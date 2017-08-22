from flask import Flask, request, render_template, redirect, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, func, update
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Dailyhours
from datetime import date, datetime

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
                request.form['work_date'], "%Y-%m-%d"), # .strftime('%A'),
            hours_worked = (request.form['hours_worked']),
            remarks = (request.form['remarks'])
            )

        session.add(new_date)
        session.commit()
        return redirect(url_for('indexPage'))
    else:
        return render_template('add_day.html')

# @app.route('/delete/', methods=['GET', 'POST'])
#def deleteDay(work_date):
#    """ Page to delete a day row entry from the database """
#    day_to_delete = session.query(Dailyhours).filter_by(work_date = work_date).one()
#    if request.method == 'POST':
#        session.delete(day_to_delete)
#        # flash('%s Successfully Deleted' % restaurantToDelete.name)
#        session.commit()
#        return redirect(url_for('indexPage', restaurant_id = restaurant_id))
#    else:
#        return render_template('deleteRestaurant.html',restaurant = restaurantToDelete)



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)