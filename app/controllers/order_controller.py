from flask import request, jsonify
from app.services.order_service import OrderService
from app.utils.exceptions import ValidationError, ResourceNotFoundError

order_service = OrderService()  # Initialize service
def create_order():
    """
    Create a new order.

    Returns:
        Response: JSON response with a success message.
    """
    try:
        data = request.get_json()
        order = order_service.create_order(
            user_id=data['user_id'],
            restaurant_id=data['restaurant_id'],
            items=data['items'],
            total_price=data['total_price']
        )
        return jsonify({"message": "Order created successfully"}), 201
    except (ValidationError, ResourceNotFoundError) as e:
        return jsonify({"message": str(e)}), 400

def get_order(order_id):
    """
    Get order details.

    Args:
        order_id (str): The ID of the order.

    Returns:
        Response: JSON response with order details or an error message.
    """
    try:
        order = order_service.get_order(order_id)
        return jsonify(order.__dict__), 200
    except ResourceNotFoundError as e:
        return jsonify({"message": str(e)}), 404

def get_user_order_status(user_id):
    """
    Get the status of orders for a user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        Response: JSON response with order statuses or an error message.
    """
    try:
        user_orders = order_service.get_user_orders(user_id)
        if user_orders:
            return jsonify([order.__dict__ for order in user_orders]), 200
        return jsonify({"message": "No orders found for this user"}), 404
    except ResourceNotFoundError as e:
        return jsonify({"message": str(e)}), 404

def update_order_status(order_id):
    """
    Update the status of an order.

    Args:
        order_id (str): The ID of the order.

    Returns:
        Response: JSON response with a success message or an error message.
    """
    try:
        data = request.get_json()
        status = data.get('status')
        role = request.headers.get('role', 'user')  # Should come from authenticated user
        order = order_service.update_order_status(order_id, status, role)
        return jsonify({"message": f"Order {status.lower()} successfully"}), 200
    except (ValidationError, ResourceNotFoundError) as e:
        return jsonify({"message": str(e)}), 400