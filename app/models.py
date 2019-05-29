# models.py file
from app import db

class Dailyhours(db.Model):
    __tablename__ = 'dailyhours'

    work_date = db.Column(db.Date, primary_key = True)
    hours_worked = db.Column(db.Float)
    remarks = db.Column(db.String(250))

    def __repr__(self):
        return '<DailyHours {}>'.format(self.work_date)