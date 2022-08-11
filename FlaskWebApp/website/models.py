from . import db
# import enum
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
# from wtforms_sqlalchemy.fields import QuerySelectField

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class Level(enum.Enum):
#     siswa = "Siswa"
#     guru = "Guru"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    level = db.Column(db.String(150))
    # level = db.Column(db.Enum(Level))
    notes = db.relationship('Note')

# class mapel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nama_mapel = db.Column(db.Integer)


# class Guru(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
#     murid = db.relationship('User', backref='guru') # karena seorang guru akan mengajar banyak murid

#  class Admin(db.Model, UserMixin):
#     email = db.Column(db.String(128),unique=True)
#     name = db.Column(db.String(128))
