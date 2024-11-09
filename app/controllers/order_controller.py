from flask import request, jsonify
from app.models.order_model import Order, orders

def create_order():
    """
    Create a new order.

    Returns:
        Response: JSON response with a success message.
    """
    data = request.get_json()
    order = Order(**data)
    orders.append(order)
    return jsonify({"message": "Order created successfully"}), 201

def get_order(order_id):
    """
    Get order details.

    Args:
        order_id (str): The ID of the order.

    Returns:
        Response: JSON response with order details or an error message.
    """
    order = next((o for o in orders if o.user_id == order_id), None)
    if order:
        return jsonify(order.__dict__), 200
    return jsonify({"message": "Order not found"}), 404

def get_user_order_status(user_id):
    """
    Get the status of orders for a user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        Response: JSON response with order statuses or an error message.
    """
    user_orders = [order for order in orders if order.user_id == user_id]
    if user_orders:
        return jsonify([order.__dict__ for order in user_orders]), 200
    return jsonify({"message": "No orders found for this user"}), 404

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
    if order and status in ['Accepted', 'Rejected', 'Picked Up', 'Delivered']:
        order.update_status(status)
        return jsonify({"message": f"Order {status.lower()} successfully"}), 200
    return jsonify({"message": "Order not found or invalid status"}), 404
