from random import choice as rc
from faker import Faker
from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()
with app.app_context():
    fake = Faker()

    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    pizzas = []
    pizza_name = ["Macaroni", "Peperoni", "Hawaian", "Bbq Chicken", "Mushroom tikitaka", "Pineapple Burst", "Spicy Peri Peri", "Cheese Burst", "Beef Loves", "Veggie Flavour"]

    for name in pizza_name:
        pizza = Pizza(name = name, ingredients = ", ".join(fake.words()))
        pizzas.append(pizza)
    
    db.session.add_all(pizzas)
    db.session.commit()


    restaurants = []
    for j in range(10):
        restaurant = Restaurant(name = fake.company(), address = fake.address())
        restaurants.append(restaurant)
    db.session.add_all(restaurants)
    db.session.commit()
    
    RestaurantPizzas = [
        RestaurantPizza(price=15, restaurant_id=1, pizza_id=1),
        RestaurantPizza(price=13, restaurant_id=1, pizza_id=2),
        RestaurantPizza(price=17, restaurant_id=2, pizza_id=3),
        RestaurantPizza(price=11, restaurant_id=2, pizza_id=4),
        RestaurantPizza(price=12, restaurant_id=3, pizza_id=5),
        RestaurantPizza(price=16, restaurant_id=3, pizza_id=6),
        RestaurantPizza(price=11, restaurant_id=4, pizza_id=7),
        RestaurantPizza(price=22, restaurant_id=5, pizza_id=8),
        RestaurantPizza(price=14, restaurant_id=5, pizza_id=1),
        RestaurantPizza(price=18, restaurant_id=4, pizza_id=2), 
    ]
    db.session.add_all(RestaurantPizzas)
    db.session.commit()



    
