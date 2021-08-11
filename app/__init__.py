import json
import mariadb
from flask import Flask
from os import environ

# Initialize application
app = Flask(__name__, static_folder=None)

config = {
    'host': environ.get('HOSTNAME'),
    'port': environ.get('PORT'),
    'user': environ.get('USER'),
    'password': environ.get('PASSWORD'),
    'database': environ.get('DATABASENAME')
}
