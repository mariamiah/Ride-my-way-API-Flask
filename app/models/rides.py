import sqlalchemy
from sqlalchemy.ext.associationproxy import association_proxy
from ..app import db, ma

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.String(255), db.ForeignKey('user.id'))
    start_time = db.Column(db.String(255), index=True, unique=True)
    destination = db.Column(db.String(255), unique=True)
    source = db.Column(db.String(255), unique=False)
    active = db.Column(db.Boolean, default=True)
    ride_date = db.Column(db.Date, nullable=False)

class RideRequest(db.Model):
    id = db.Column(db.String(32), nullable=False, primary_key=True)
    rid = db.Column(db.String(255), db.ForeignKey('ride.id'))
    passenger_id = db.Column(db.String(255), db.ForeignKey('user.id'))
    status = db.Column(db.Boolean, default=False, nullable=False)
