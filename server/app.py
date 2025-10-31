from flask import Flask
from flask_restful import Resource, Api
from flask_migrate import Migrate
from model import db, Car, Dealer

# creates the first flask instance of app
app = Flask(__name__)

# wraps the app with Flask-restfulls API class.
api = Api(app)


# configuring the database
app.config['SQLALCHEMY-DATABASE-URI'] = 'sqlite:///auto.db'
app.config['SQLALCHEMY-TRACK-MODIFICATIONS'] = False

db.init_app()
migrate=Migrate(db, app)



