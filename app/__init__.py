import json
import mariadb
import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import environ
from sqlalchemy.ext.declarative import declarative_base

# Initialize application
app = Flask(__name__, static_folder=None)
app.config["SQLALCHEMY_DATABASE_URI"] = "mariadb+mariadbconnector://"+\
environ.get('USER')+":"+environ.get('PASSWORD')+"@"+\
environ.get('HOSTNAME')+":"+environ.get('PORT')+"/"+\
environ.get('DATABASENAME')

db = SQLAlchemy(app)
ma = Marshmallow(app)

from .models.users import User, Relationship, UserSchema
from .models.rides import Ride, RideRequest

db.create_all()
