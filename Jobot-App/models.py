from flask_sqlalchemy import SQLAlchemy
from main import app
from main import db
from utils import id_generator
from werkzeug.security import generate_password_hash, check_password_hash


class Registered_User_Details(db.Model):
    __tablename__ = 'Registered_User_Details'
    userid = db.Column('userid', db.Integer, primary_key=True)
    username = db.Column('username', db.String(100), unique=True)
    password = db.Column('password', db.String(100), unique=True)

    def __init__(self, username, password):
        #self.userid = userid
        self.username = username
        self.password = password
