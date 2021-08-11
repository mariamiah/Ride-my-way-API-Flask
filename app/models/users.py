import sqlalchemy
from ..app import Base, ma

class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    email = sqlalchemy.Column(sqlalchemy.String(length=100))
    password = sqlalchemy.Column(sqlalchemy.String(length=100))
    
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

class UserSchema(ma.Schema):
    class Meta:
        # fields to expose
        fields = ("email", "date_created", "first_name", "last_name", "_links")
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("user_detail", values=dict(id="<id>")),
            "collection": ma.URLFor("users"),
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)
