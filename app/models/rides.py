from .. import db, ma

class Ride(db.Model):
    """Data model for Rides."""

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    start_time = db.Column(db.String(255), index=True, unique=True)
    destination = db.Column(db.String(255), unique=True)
    source = db.Column(db.String(255), unique=False)
    active = db.Column(db.Boolean, default=True)
    ride_date = db.Column(db.Date, nullable=False)

class RideRequest(db.Model):
    """Data model for ride requests."""

    id = db.Column(db.String(32), nullable=False, primary_key=True)
    rid = db.Column(db.Integer, db.ForeignKey('ride.id'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Boolean, default=False, nullable=False)


class RideSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Ride
    id = ma.auto_field()
    driver_id = ma.auto_field()
    start_time = ma.auto_field()
    destination = ma.auto_field()
    source = ma.auto_field()
    active = ma.auto_field()
    ride_date = ma.auto_field()
