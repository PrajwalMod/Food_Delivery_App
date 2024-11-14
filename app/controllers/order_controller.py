from flask import request, jsonify
from app.models.order_model import Order
from app.database import db

def create_order(data):
    """
    Create a new order.

    Returns:
        Response: JSON response with a success message and order_id.
    """
    try:
        order = Order(
            user_id=data['user_id'],
            restaurant_id=data['restaurant_id'],
            items=data['items'],
            total_price=data['total_price']
        )
        db.session.add(order)
        db.session.commit()
        return jsonify({"message": "Order created successfully", "order_id": order.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Failed to create order: {str(e)}"}), 400

def get_order(order_id):
    """
    Get order details.

    Args:
        order_id (str): The ID of the order.

    Returns:
        Response: JSON response with order details or an error message.
    """
    order = Order.query.get(order_id)
    if order:
        return jsonify({
            "id": order.id,
            "user_id": order.user_id,
            "restaurant_id": order.restaurant_id,
            "items": order.items,
            "total_price": order.total_price,
            "status": order.status
        }), 200
    return jsonify({"message": "Order not found"}), 404

def get_user_order_status(user_id):
    """
    Get the status of orders for a user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        Response: JSON response with order statuses or an error message.
    """
    user_orders = Order.query.filter_by(user_id=user_id).all()
    if user_orders:
        return jsonify([
            {
                "id": order.id,
                "user_id": order.user_id,
                "restaurant_id": order.restaurant_id,
                "items": order.items,
                "total_price": order.total_price,
                "status": order.status
            } for order in user_orders
        ]), 200
    return jsonify({"message": "No orders found for this user"}), 404

def update_order_status(order_id, status):
    """
    Update order status.

    Args:
        order_id (str): The ID of the order.
        status (str): The new status of the order.

    Returns:
        Response: JSON response with a success message or an error message.
    """
    order = Order.query.get(order_id)
    if order and status in ['Accepted', 'Rejected']:
        order.status = status
        db.session.commit()
        return jsonify({"message": f"Order {status.lower()} successfully"}), 200
    return jsonify({"message": "Order not found or invalid status"}), 404
