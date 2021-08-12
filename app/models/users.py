import sqlalchemy
from sqlalchemy.ext.associationproxy import association_proxy
from .. import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False)
    username = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=False)
    phone_number = db.Column(db.String(255), unique=True)
    role = db.Column(db.String(255))
    requested_rels = db.relationship(
        'Relationship',
        foreign_keys='Relationship.requesting_user_id',
        backref='requesting_user' 
    )
    received_rels = db.relationship(
        'Relationship',
        foreign_keys='Relationship.receiving_user_id',
        backref='receiving_user'
    )
    aspiring_friends = association_proxy('received_rels', 'requesting_rels')
    desired_friends = association_proxy('requested_rels', 'receiving_user')

    def __repr__(self):
        return '<User %r>' % (self.username)


class Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requesting_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    receiving_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    status = db.Column(db.Integer)

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
    id = ma.auto_field()
    name = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()
    phone_number = ma.auto_field()
    role = ma.auto_field()

user_schema = UserSchema()
users_schema = UserSchema(many=True)
