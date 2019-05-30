from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField
from wtforms.validators import DataRequired

from .util.validators import Unique
from app.models import Dailyhours
from app import db

class AddDayForm(FlaskForm):
    new_date = DateField('New Date', format='%Y-%m-%d', \
        validators=[DataRequired(),
        Unique(
            Dailyhours,
            Dailyhours.work_date,
            message='This date already has an entry')])
    hours_worked = FloatField('Hours Worked', validators=[DataRequired()])
    remarks = StringField('Remarks')
    submit = SubmitField('Submit')

class EditDayForm(FlaskForm):
    hours_worked = FloatField('Hours Worked', validators=[DataRequired()])
    remarks = StringField('Remarks')
    submit = SubmitField('Submit')

class DeleteDayForm(FlaskForm):
    submit = SubmitField('DELETE')

