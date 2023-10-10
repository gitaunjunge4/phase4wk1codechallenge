from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

from models import Restaurant, Pizza, RestaurantPizza, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.json.compact = False

migrate = Migrate(app, db, render_as_batch=True)
db.init_app(app)

api = Api(app)

# "landing" page
class Home(Resource):
    def get(self):
        response_dict = {
            "Home page": "Welcome to the Restauraunt page",
        }
        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response

api.add_resource(Home, '/')


class Restaurants(Resource):
    # GET for restaurants
    def get(self):
        response_dict_list = [n.to_dict() for n in Restaurant.query.all()]
        response = make_response(
            jsonify(response_dict_list),
            200,
        )
        return response

    # POST for restaurants
    def post(self):
        new_restaurant = Restaurant(
            name=request.form['name'],
            address=request.form['address'],
        )

        db.session.add(new_restaurant)
        db.session.commit()

        response_dict= new_restaurant.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )
        return response

api.add_resource(Restaurants, '/restaurants')



class RestaurantById(Resource):
    # GET for restaurantbyID
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            response = make_response(
                jsonify(restaurant.to_dict()),
                200,
            )
            return response
        else:
            response = jsonify({"message": "Not Found"})
            return response, 404
        
    # DELETE for restaurantbyID
    def delete(self, id):
        restaurant = Restaurant.query.get(id)

        if restaurant:
            Restaurant.query.filter_by(id=id).delete

            db.session.delete(restaurant)
            db.session.commit()

            response = jsonify({"message": "Restaurant successfully deleted"})
            return response, 200
        else:
            response = jsonify({"message": "Not Found"})
            return response, 404
      
api.add_resource(RestaurantById, '/restaurants/<int:id>')


class Pizzas(Resource):
    # GET for Pizzas
    def get(self):
        response_dict_list = [n.to_dict() for n in Pizza.query.all()]

        response = make_response(
            jsonify(response_dict_list),
            200,
        )
        return response
    
api.add_resource(Pizzas, '/pizzas')


class RestaurantPizzas(Resource):

    def get(self):
        response_dict_list = [n.to_dict() for n in RestaurantPizza.query.all()]
        response = make_response(
            jsonify(response_dict_list),
            200,
        )
        return response

    def post(self):
        data = request.get_json()
        
        price=data.get('price')
        pizza_id=data.get('pizza_id')
        restaurant_id=data.get('restaurant_id')

        if pizza_id and restaurant_id:
            new_restaurant_pizza = RestaurantPizza(
                price=price,
                pizza_id=pizza_id,
                restaurant_id=restaurant_id
            )

            db.session.add(new_restaurant_pizza)
            db.session.commit()

            pizza = Pizza.query.get(pizza_id)
            if pizza:
                response = make_response(
                    {"id": pizza.id,
                    "ingredients" : pizza.ingredients,
                    "name" : pizza.name},
                    201
                )
                return response
            
            else:  
                response = jsonify({"message": "Not Found"}) 
                return response, 404

api.add_resource(RestaurantPizzas, '/restaurant_pizzas')

if __name__ == "__main__":
    app.run(debug=True, port=5555)