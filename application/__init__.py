# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv


# create a new instance of Flask and store it in app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/Exercise18"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


# link our app to the persistence layer
db = SQLAlchemy(app)