from src.db.core import db
from enum import Enum
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Role(Enum):
    USERS = 0
    ADMIN = 1

class Admin(db.Model, UserMixin):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.Enum(Role), default=Role.ADMIN)
    
    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)
    