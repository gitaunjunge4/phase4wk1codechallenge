PHASE 4 WEEK1 CODE CHALLENGE

PIZZA RESTAURANT
    The Restaurant API is a robust web service designed to manage restaurant and pizza-related information efficiently.
    This API enables users to perform various operations, including retrieving restaurant details, managing pizza data, and associating pizzas with specific restaurants. 
    It is built using Flask, SQLAlchemy.

INSTALLATION
    -Clone this repo

    -Navigate to the project directory using cd

    -Create a virtual environment (optional but recommended)

    -Activate the virtual environment

    -Install the project dependencies

    -Apply the database migrations to create a db: 
        1. flask db init 
        2. flask db migrate 
        3. flask db upgrade

FEATURES
    The Restaurant API offers the following key features:

    -Retrieve Restaurants: Get a list of all registered restaurants, including their names and addresses.

    -Retrieve Pizzas: Fetch a list of all available pizzas, complete with details like ingredients and creation/update times.

    -Retrieve Specific Restaurant: Get detailed information about a specific restaurant by providing its unique ID.

    -Retrieve Specific Pizza: Get detailed information about a specific pizza by providing its unique ID.

    -Delete Restaurant: Delete a restaurant, including all associated records by specifying its unique ID.

    -Delete Pizza:  Delete a pizza, including all associated records by specifying its unique ID.

    -Retrieve Restaurant-Pizza Associations: Fetch a list of all restaurant-pizza associations, including prices.

    -Create Restaurant-Pizza Association: Create a new restaurant-pizza association, specifying the pizza, restaurant, and price

ENDPOINTS
    The following endpoints are available:

        -GET /restaurants: Retrieve a list of all registered restaurants.
        -GET /restaurants/< int:id> Get details of a specific restaurant by its ID.
        -DELETE /restaurants/< int:id>Delete a restaurant by its ID.
        -GET /pizzas: Retrieve a list of all available pizzas.
        -GET /pizzas/< int:id> Get details of a specific pizza by its ID.
        -DELETE /pizzas/< int:id> Delete a pizza by its ID.
        -GET /restaurantspizza: Fetch a list of restaurant-pizza associations.
        -POST /restaurantspizza: Create a new restaurant-pizza association, specifying the pizza, restaurant, and price.
 

MODELS
    The Restaurant API includes three main models:

    Restaurant: 
    -Represents a restaurant with attributes such as name and address. 
    -Restaurants can be associated with multiple pizzas.

    Pizza: 
    -Represents a pizza with attributes such as name, ingredients, and creation/update times. 
    -Pizzas can be associated with multiple restaurants.

    RestaurantPizza: 
    -Represents the association between restaurants and pizzas, including the price. 
    -This model allows you to associate a pizza with a specific restaurant along with its price.


AUTHOR
Gitau Njung'e 

