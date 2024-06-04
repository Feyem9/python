from sqlalchemy.sql import func
from config import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100) , nullable=False)
    author = db.Column(db.String(50) , nullable=False)
    description = db.Column(db.String(500) , nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default = func.now())
