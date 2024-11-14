from app.models.restaurant_model import Restaurant, restaurants

def add_restaurant(data):
    """
    Add a new restaurant.

    Args:
        data (dict): A dictionary containing restaurant details.

    Returns:
        Restaurant: The created restaurant object.
    """
    # Ensure required fields are provided in the data
    required_fields = ['name', 'address', 'cuisine', 'menu', 'work_hours']
    if not all(field in data for field in required_fields):
        raise ValueError("Missing required fields: name, address, cuisine, menu, work_hours")

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
    restaurant = next((r for r in restaurants if r.name == restaurant_id), None)
    if not restaurant:
        raise ValueError(f"Restaurant with name {restaurant_id} not found")
    return restaurant
