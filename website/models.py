from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
# from flask_mail import Mail,Message




class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))
    phoneNumber = db.Column(db.String(12), unique=True, nullable=False)
    idNumber = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    notes = db.relationship('Note')

class Conta(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    yourname = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(12), unique=True, nullable=False)
    message = db.Column(db.String(1500))


class Urgence_user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    phoneNumber = db.Column(db.String(12), unique=True, nullable=False)
    adress = db.Column(db.String(150), unique=True, nullable=False)





