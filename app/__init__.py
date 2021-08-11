import json
import mariadb
import sqlalchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from os import environ
from sqlalchemy.ext.declarative import declarative_base

# Initialize application
app = Flask(__name__, static_folder=None)
ma = Marshmallow(app)
Base = declarative_base()
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://"+
environ.get('USER')+":"+environ.get('PASSWORD')+"@"+
environ.get('HOSTNAME')+":"+environ.get('PORT')+"/"+
environ.get('DATABASENAME'))
