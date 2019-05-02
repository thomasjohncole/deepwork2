# this is the __init__.py file
from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# lower case 'config' is the module name
# upper case 'Config' is the class name
app.config.from_object(Config)

Bootstrap(app)

from app import routes
