from flask import request, jsonify
from app.models.restaurant_model import Restaurant, restaurants
from app.models.order_model import Order, orders

def add_restaurant():
    """
    Add a new restaurant.

    Returns:
        Response: JSON response with a success message.
    """
    data = request.get_json()
    restaurant = Restaurant(**data)
    restaurants.append(restaurant)
    return jsonify({"message": "Restaurant added successfully"}), 201

def get_restaurant(restaurant_id):
    """
    Get restaurant details.

    Args:
        restaurant_id (str): The ID of the restaurant.

    Returns:
        Response: JSON response with restaurant details or an error message.
    """
    restaurant = next((r for r in restaurants if r.name == restaurant_id), None)
    if restaurant:
        return jsonify(restaurant.__dict__), 200
    return jsonify({"message": "Restaurant not found"}), 404

def update_restaurant(restaurant_id):
    """
    Update restaurant details.

    Args:
        restaurant_id (str): The ID of the restaurant.

    Returns:
        Response: JSON response with a success message or an error message.
    """
    data = request.get_json()
    restaurant = next((r for r in restaurants if r.name == restaurant_id), None)
    if restaurant:
        restaurant.update_details(**data)
        return jsonify({"message": "Restaurant details updated successfully"}), 200
    return jsonify({"message": "Restaurant not found"}), 404

def update_order_status(order_id):
    """
    Update the status of an order.

    Args:
        order_id (str): The ID of the order.

    Returns:
        Response: JSON response with a success message or an error message.
    """
    data = request.get_json()
    status = data.get('status')
    order = next((o for o in orders if o.user_id == order_id), None)
    if order and status in ['Accepted', 'Rejected']:
        order.update_status(status)
        return jsonify({"message": f"Order {status.lower()} successfully"}), 200
    return jsonify({"message": "Order not found or invalid status"}), 404

def search_restaurants():
    """
    Search for restaurants based on query parameters.

    Returns:
        Response: JSON response with a list of matching restaurants.
    """
    cuisine = request.args.get('cuisine')
    max_price = request.args.get('max_price', type=float)
    results = restaurants

    if cuisine:
        results = [r for r in results if r.cuisine.lower() == cuisine.lower()]

    if max_price is not None:
        results = [r for r in results if any(item['price'] <= max_price for item in r.menu)]

    return jsonify([r.__dict__ for r in results]), 200
