from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY') #environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')  #environment variable

db = SQLAlchemy(app)

from personal_blog import routes