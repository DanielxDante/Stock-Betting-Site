from . import db # importing from current directory
from flask_login import UserMixin #flask inbuilt library for user login, if doing from scratch, we dont need this
from sqlalchemy.sql import func # enables general stuff like time and date

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # foreign key; allows each user to have many notes; note lowercase U when referencing it in SQL

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True) # doesnt have to be an integer; automatically increments id by one when adding into the database
    email = db.Column(db.String(150), unique = True) # 150 represents the string length; unique means no other user can have the same enail
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # list of notes; note capital N, its not very consistent in naming conventions...
