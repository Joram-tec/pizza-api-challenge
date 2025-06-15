from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from server.app import db


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float, nullable = False)


    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    @validates('price')
    def validate_price(self, key, value):
        if value < 1 or value > 30:
            raise ValueError("Price must be between 1 and 30")
        return value

    def __repr__(self):
        return f'<RestaurantPizza ${self.price} {self.id} {self.pizza.to_dict()} {self.restaurant.to_dict()}>'