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

class Restaurants(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in Restaurant.query.all()]

        response = make_response(
            response_dict_list,
            200
        )
        return response



if __name__ == "__main__":
    app.run(debug=True, port=5555)