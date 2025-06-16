from flask_sqlalchemy import SQLAlchemy
from server.app import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship("RestaurantPizza", back_populates="pizza", overlaps="restaurants", cascade="all, delete-orphan")
    restaurants = db.relationship("Restaurant", secondary="restaurant_pizzas", back_populates="pizzas", viewonly=True )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients
        }
