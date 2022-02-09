from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class import os

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI']