#  Pizza API - Flask RESTFUL Backend

Welcome to the Pizza API project! This Flask-based RESTful API manages pizza restaurants, pizzas, and the pricing of pizzas at different restaurants.

### Author
### Joram Wayne (Joram-tec)



## Project Structure

- pizza-api-challenge/
- │
- ├── server/
- │ ├── init.py
- │ ├── app.py
- │ ├── models/
- │ │ ├── init.py
- │ │ ├── pizza.py
- │ │ ├── restaurant.py
- - │ │ └── restaurant_pizza.py
- │ ├── routes/
- │ │ ├── pizza_routes.py
- │ │ ├── restaurant_routes.py
- │ │ └── restaurant_pizza_routes.py
- │ └── seed.py
- │
- ├── migrations/
- ├── app.db
- ├── README.md
- ├── requirements.txt
- └── .flaskenv

##  Features

- View all pizzas 
- View all restaurants 
- View all pizza-restaurant price listings 
- Create a new restaurant-pizza entry
- Search by pizza name or restaurant ID

##  Technologies Used

- Python 3.8+
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite
- Faker (for seed data)

### 1. Clone the Repo

- git clone git@github.com:Joram-tec/pizza-api-challenge.git


### 2. Create & Activate Virtual Environment

- python3 -m venv env
 source env/bin/activate 
-
### 3. Install Dependencies

- pipenv install flask flask_sqlalchemy flask_migrate
- pipenv shell

### 4. Run Migrations

- flask db init
- flask db migrate -m "Initial migration"
- flask db upgrade

### 5. Seed the Database

- python -m server.seed

### 6. Run the Server

- flask run 

### 7. See the result on browser:
- http://127.0.0.1:5000 and add a valid route eg. /pizzas after the ULR

### API Endpoints

# GET, POST, DELETE 
# pizzas, restaurants, restraunt_pizzas

###  Search in Postman

# Find pizza by ID:
-  GET http://127.0.0.1:5000/pizzas/1

# Find restaurant by ID:
-  GET http://127.0.0.1:5000/restaurants/1


###  Testing with Flask Shell
-  flask shell

-  from server.models.pizza import Pizza
-  Pizza.query.all()

### License
# MIT LICENSE