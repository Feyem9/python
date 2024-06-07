from sqlalchemy.sql import func
from config import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    username = db.Column(db.String(100) , nullable=False)
    email = db.Column(db.String(150) , nullable=False)
    password = db.Column(db.String(500) , nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default = func.now())