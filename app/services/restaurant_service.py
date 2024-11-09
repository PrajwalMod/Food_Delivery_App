from app.models.restaurant_model import Restaurant, restaurants

def add_restaurant(data):
    """
    Add a new restaurant.

    Args:
        data (dict): A dictionary containing restaurant details.

    Returns:
        Restaurant: The created restaurant object.
    """
    restaurant = Restaurant(**data)
    restaurants.append(restaurant)
    return restaurant

def get_restaurant_by_id(restaurant_id):
    """
    Get a restaurant by its ID.

    Args:
        restaurant_id (str): The ID of the restaurant.

    Returns:
        Restaurant: The restaurant object if found, else None.
    """
    return next((r for r in restaurants if r.name == restaurant_id), None)
