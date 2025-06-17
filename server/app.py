from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from server.models.pizza import Pizza
    from server.models.restaurant import Restaurant
    from server.models.restaurant_pizza import RestaurantPizza

  
    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        return jsonify([pizza.to_dict() for pizza in Pizza.query.all()]), 200

    @app.route('/pizzas/<int:id>', methods=['GET'])
    def get_pizza(id):
        pizza = Pizza.query.get(id)
        if pizza:
            return jsonify(pizza.to_dict()), 200
        return jsonify({"error": "Pizza not found"}), 404

    @app.route('/pizzas', methods=['POST'])
    def create_pizza():
        data = request.get_json()
        try:
            new_pizza = Pizza(name=data['name'], ingredients=data['ingredients'])
            db.session.add(new_pizza)
            db.session.commit()
            return jsonify(new_pizza.to_dict()), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/pizzas/<int:id>', methods=['DELETE'])
    def delete_pizza(id):
        pizza = Pizza.query.get(id)
        if pizza:
            db.session.delete(pizza)
            db.session.commit()
            return jsonify({"message": "Pizza deleted"}), 200
        return jsonify({"error": "Pizza not found"}), 404


    @app.route('/restaurants', methods=['GET'])
    def get_restaurants():
        return jsonify([restaurant.to_dict() for restaurant in Restaurant.query.all()]), 200

    @app.route('/restaurants/<int:id>', methods=['GET'])
    def get_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            return jsonify(restaurant.to_dict()), 200
        return jsonify({"error": "Restaurant not found"}), 404

    @app.route('/restaurants', methods=['POST'])
    def create_restaurant():
        data = request.get_json()
        try:
            new_restaurant = Restaurant(name=data['name'], address=data['address'])
            db.session.add(new_restaurant)
            db.session.commit()
            return jsonify(new_restaurant.to_dict()), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/restaurants/<int:id>', methods=['DELETE'])
    def delete_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return jsonify({"message": "Restaurant deleted"}), 200
        return jsonify({"error": "Restaurant not found"}), 404

   
    @app.route('/restaurant_pizzas', methods=['GET'])
    def get_restaurant_pizzas():
        return jsonify([rp.to_dict() for rp in RestaurantPizza.query.all()]), 200

    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.get_json()
        try:
            new_rp = RestaurantPizza(
                price=data['price'],
                pizza_id=data['pizza_id'],
                restaurant_id=data['restaurant_id']
            )
            db.session.add(new_rp)
            db.session.commit()
            return jsonify(new_rp.to_dict()), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/restaurant_pizzas/<int:id>', methods=['DELETE'])
    def delete_restaurant_pizza(id):
        rp = RestaurantPizza.query.get(id)
        if rp:
            db.session.delete(rp)
            db.session.commit()
            return jsonify({"message": "RestaurantPizza deleted"}), 200
        return jsonify({"error": "RestaurantPizza not found"}), 404

    return app
