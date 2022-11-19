import flask
import os 
import pytz
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

try:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
except:
    app.config.from_pyfile("config.py")

# time setup for the server side time
eastern = pytz.timezone('America/New_York')

db = SQLAlchemy(app)
