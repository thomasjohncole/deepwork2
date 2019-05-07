from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField
from wtforms.validators import DataRequired

class AddDayForm(FlaskForm):
    new_date = DateField('New Date', format='%Y-%m-%d', \
        validators=[DataRequired()])
    hours_worked = FloatField('Hours Worked', validators=[DataRequired()])
    remarks = StringField('Remarks')
    submit = SubmitField('Submit')

class EditDayForm(FlaskForm):
    hours_worked = FloatField('Hours Worked', validators=[DataRequired()])
    remarks = StringField('Remarks')
    submit = SubmitField('Submit')

class DeleteDayForm(FlaskForm):
    submit = SubmitField('YES!')

