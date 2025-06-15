from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()
        new_rp = RestaurantPizza(price=data['price'], pizza_id=data['pizza_id'], restaurant_id=data['restaurant_id'])
        db.session.add(new_rp)
        db.session.commit()

        pizza = Pizza.query.get(data['pizza_id'])
        restaurant = Restaurant.query.get(data['restaurant_id'])

        return jsonify({
            "id": new_rp.id,
            "price": new_rp.price,
            "pizza_id": new_rp.pizza_id,
            "restaurant_id": new_rp.restaurant_id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
