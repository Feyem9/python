import os

from flask_sqlalchemy import SQLAlchemy #type:ignore

db = SQLAlchemy()
SECRET_KEY = os.urandom(32)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Feyem.111@127.0.0.1:3306/flask_blog_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False