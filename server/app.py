from flask import Flask 
from flask_restful import Resource, Api
from flask_migrate import Migrate


app = Flask(__name__)
api = Api(app)

