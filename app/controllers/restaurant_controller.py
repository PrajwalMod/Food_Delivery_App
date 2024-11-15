from flask import request, jsonify
from app.models.restaurant_model import Restaurant
from app.models.order_model import Order
from app.database import db

def add_restaurant(data):
    """
    Add a new restaurant.

    Returns:
        Response: JSON response with a success message.
    """
    try:
        restaurant = Restaurant(
            name=data['name'],
            address=data['address'],
            cuisine=data['cuisine'],
            menu=data['menu'],
            work_hours=data['work_hours']
        )
        db.session.add(restaurant)
        db.session.commit()
        return jsonify({"message": "Restaurant added successfully", "restaurant_id": restaurant.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Failed to add restaurant: {str(e)}"}), 400

def get_restaurant(restaurant_id):
    """
    Get restaurant details.

    Args:
        restaurant_id (str): The ID of the restaurant.

    Returns:
        Response: JSON response with restaurant details or an error message.
    """
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        return jsonify({
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "cuisine": restaurant.cuisine,
            "menu": restaurant.menu,
            "work_hours": restaurant.work_hours
        }), 200
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
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        try:
            restaurant.update_details(
                address=data.get('address'),
                cuisine=data.get('cuisine'),
                menu=data.get('menu'),
                work_hours=data.get('work_hours')
            )
            db.session.commit()
            return jsonify({"message": "Restaurant details updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": f"Failed to update restaurant: {str(e)}"}), 400
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
    order = Order.query.get(order_id)
    if order and status in ['Accepted', 'Rejected']:
        order.update_status(status)
        db.session.commit()
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
    query = Restaurant.query

    if cuisine:
        query = query.filter(Restaurant.cuisine.ilike(f"%{cuisine}%"))

    restaurants = query.all()
    if max_price is not None:
        restaurants = [
            restaurant for restaurant in restaurants
            if any(item['price'] <= max_price for item in restaurant.menu)
        ]

    return jsonify([
        {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "cuisine": restaurant.cuisine,
            "menu": restaurant.menu,
            "work_hours": restaurant.work_hours
        } for restaurant in restaurants
    ]), 200

def list_all_restaurants():
    restaurants = Restaurant.query.all()  # Retrieve all restaurants
    restaurant_list = [{
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "cuisine": restaurant.cuisine,
        "menu": restaurant.menu,
        "work_hours": restaurant.work_hours
    } for restaurant in restaurants]
    return jsonify(restaurant_list), 200