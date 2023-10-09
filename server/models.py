from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# Restaurant Model
class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String)

    pizzas = db.relationship(
        'Pizza', 
        secondary="restaurant_pizzas",
        backref='Restaurant'
        )
    
    def repr(self):
        return f"Name: {self.name}, Address: {self.address}"
    
    @validates("name")
    def validate_name(self, key, name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 letters.")
        else:
            return name
    

# Pizza Model
class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurants = db.relationship(
        "Restaurant", 
        secondary="restaurant_pizzas", 
        backref="Pizza"
    )

    def repr(self):
        return f"Name: {self.name}, Ingredients: {self.ingredients}, {self.created_at} {self.updated_at}"
    

# RestaurantPizza Model
class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    restaurant = db.relationship("Restaurant", backref=db.backref("restaurant_pizzas"))
    pizza = db.relationship("Pizza", backref=db.backref("restaurant_pizzas"))

    def repr(self):
        return f"RestaurantPizza {self.restaurant.name} - {self.pizza.name}"
    
    @validates('price')
    def validate_price(self, key, price):
        if price not in range(1, 31):
            raise ValueError("Price must be between 1 and 30.")
        else:
            return price

