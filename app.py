# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pubhub.db'
app.secret_key = "Xjp02u"

db = sa(app)
