# work.py file - this is the main app file as defined in .flaskenv
from app import app, db
# imports the app variable, from the app package
# the app variable is actually an instance of the Flask class
# which is imported from the flask package, in the venv directory
# below imports aid in testing from the shell
from app.models import Dailyhours
from datetime import date, datetime

# creates a shell context which can be invoked by 'flask shell'
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Dailyhours': Dailyhours}