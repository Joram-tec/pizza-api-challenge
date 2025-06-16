from flask import Flask, jsonify
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

    @app.route('/pizzas')
    def get_pizzas():
        return jsonify([pizza.to_dict() for pizza in Pizza.query.all()])
    
    @app.route('/pizzas/<int:id>', methods=['GET'])
    def get_pizza(id):
        pizza = Pizza.query.get(id)
        if pizza:
            return jsonify(pizza.to_dict()), 200
        return jsonify({"error": "Pizza not found"}), 404
    

    @app.route('/pizzas/search')
    def search_pizza_by_name():
        name = request.args.get('name')
        pizza = Pizza.query.filter_by(name=name).first()
        if pizza:
            return jsonify(pizza.to_dict())
        return jsonify({"error": "Pizza not found"}), 404

    @app.route('/restaurants')
    def get_restaurants():
        return jsonify([restaurant.to_dict() for restaurant in Restaurant.query.all()])
    

    @app.route('/restaurants/<int:id>')
    def get_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            return jsonify(restaurant.to_dict())
        return jsonify({"error": "Restaurant not found"}), 404

    @app.route('/restaurant_pizzas')
    def get_restaurant_pizzas():
        return jsonify([rp.to_dict() for rp in RestaurantPizza.query.all()])

    return app
