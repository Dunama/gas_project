from src.db.core import db
from enum import Enum
from flask_login import UserMixin

class Role(Enum):
    USERS = 0
    ADMIN = 1

class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.Enum(Role), default=Role.USERS)
    

  