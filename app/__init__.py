# this is the __init__.py file
from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_datepicker import datepicker

app = Flask(__name__)

# lower case 'config' is the module name
# upper case 'Config' is the class name
app.config.from_object(Config)

Bootstrap(app)
datepicker(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
