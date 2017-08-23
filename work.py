from flask import Flask, request, render_template, redirect, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, func, update
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Dailyhours
from datetime import date, datetime
# add import for making custom converter class
from werkzeug.routing import BaseConverter, ValidationError

engine = create_engine('sqlite:///deepwork.db')
Base.metadata.bind = engine
# binds the engine to the Base class
# makes the connections between class definitions & corresponding tables in db
DBSession = sessionmaker(bind = engine)
# creates sessionmaker object, which establishes link of
# communication between our code executions and the engine we created
session = DBSession()
# create an instance of the DBSession  object - to make a changes
# to the database, we can call a method within the session

# Add custom converter - https://stackoverflow.com/questions/31669864/date-in-flask-url
class DateConverter(BaseConverter):
    """Extracts a ISO8601 date from the path and validates it."""

    regex = r'\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        try:
            return datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')


app.url_map.converters['date'] = DateConverter


@app.route('/')
def indexPage():
    """ Shows the list of workdays"""
    total_hours = session.query(func.sum(Dailyhours.hours_worked)).one()
    list = session.query(Dailyhours).order_by(Dailyhours.work_date)
    return render_template('index.html', list = list, total_hours = total_hours)

@app.route('/add/', methods=['GET', 'POST'])
def addDay():
    """ Form to add a new work day entry, and logic to POST it to db """
    if request.method == 'POST':
        new_date = Dailyhours(
            work_date = datetime.strptime(
                request.form['work_date'], "%Y-%m-%d"),
            hours_worked = (request.form['hours_worked']),
            remarks = (request.form['remarks'])
            )

        session.add(new_date)
        session.commit()
        return redirect(url_for('indexPage'))
    else:
        return render_template('add_day.html')

@app.route('/delete/<date:work_date>/', methods=['GET', 'POST'])
def deleteDay(work_date):
    """ Page to delete a day row entry from the database """
    day_to_delete = session.query(Dailyhours).filter_by(work_date = work_date).one()

    if request.method == 'POST':
        session.delete(day_to_delete)
        session.commit()
        # flash message here
        return redirect(url_for('indexPage'))
    else:
         return render_template('delete_day.html', day_to_delete = day_to_delete)


@app.route('/edit/<date:work_date>/', methods=['GET', 'POST'])
def editDay(work_date):
    """ Page to edit a day row entry from the database """
    day_to_edit = session.query(Dailyhours).filter_by(work_date = work_date).one()

    if request.method == 'POST':
        data = ({'work_date': datetime.strptime(request.form['work_date'], "%Y-%m-%d"),
                'hours_worked': request.form['hours_worked'],
                'remarks': request.form['remarks']}
                )
        session.query(Dailyhours).filter_by(work_date = work_date).update(data)
        session.commit()
        return redirect(url_for('indexPage'))
    else:
         return render_template('edit_day.html', day_to_edit = day_to_edit)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)