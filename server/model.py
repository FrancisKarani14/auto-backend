
from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# creating the models for


# Dealers model

class Dealer(db.Model, SerializerMixin):
    __tablename__ = "dealers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.string(20), nullable=False)

    # relationships
    cars = db.relationship('Car', backref='cars')

    # serialize rules


# cars model
class Car(db.Model, SerializerMixin):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    dealer_id = db.Column(db.Integer, db.Foreignkey('dealers.id'))
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    yom = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    # serialize rules
