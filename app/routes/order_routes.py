from flask import Blueprint
from app.controllers.order_controller import create_order, get_order, update_order_status, get_user_order_status
from app.middlewares.role_middleware import role_required

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/', methods=['POST'])
def create_order_route():
    """
    Create a new order
    ---
    tags:
      - Orders
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - user_id
            - restaurant_id
            - items
            - total_price
          properties:
            user_id:
              type: string
            restaurant_id:
              type: string
            items:
              type: array
              items:
                type: string
            total_price:
              type: number
    responses:
      201:
        description: Order created successfully
    """
    return create_order()

@order_bp.route('/<order_id>', methods=['GET'])
def get_order_route(order_id):
    """
    Get order details
    ---
    tags:
      - Orders
    parameters:
      - in: path
        name: order_id
        type: string
        required: true
    responses:
      200:
        description: Order details retrieved successfully
    """
    return get_order(order_id)

@order_bp.route('/user/<user_id>/status', methods=['GET'])
def get_user_order_status_route(user_id):
    """
    Get the status of orders for a user
    ---
    tags:
      - Orders
    parameters:
      - in: path
        name: user_id
        type: string
        required: true
    responses:
      200:
        description: Order statuses retrieved successfully
    """
    return get_user_order_status(user_id)

@order_bp.route('/<order_id>/status', methods=['PUT'])
@role_required('restaurant owner')
def update_order_status_route(order_id):
    """
    Update order status
    ---
    tags:
      - Orders
    parameters:
      - in: path
        name: order_id
        type: string
        required: true
      - in: body
        name: body
        schema:
          type: object
          required:
            - status
          properties:
            status:
              type: string
              enum:
                - Accepted
                - Rejected
                - Picked Up
                - Delivered
    responses:
      200:
        description: Order status updated successfully
    """
    return update_order_status(order_id)

@order_bp.route('/<order_id>/pickup', methods=['PUT'])
@role_required('delivery agent')
def pickup_order_route(order_id):
    """
    Update order status to picked up
    ---
    tags:
      - Orders
    parameters:
      - in: path
        name: order_id
        type: string
        required: true
      - in: body
        name: body
        schema:
          type: object
          required:
            - status
          properties:
            status:
              type: string
              enum:
                - Picked Up
    responses:
      200:
        description: Order status updated to picked up successfully
    """
    return update_order_status(order_id)

@order_bp.route('/<order_id>/deliver', methods=['PUT'])
@role_required('delivery agent')
def deliver_order_route(order_id):
    """
    Update order status to delivered
    ---
    tags:
      - Orders
    parameters:
      - in: path
        name: order_id
        type: string
        required: true
      - in: body
        name: body
        schema:
          type: object
          required:
            - status
          properties:
            status:
              type: string
              enum:
                - Delivered
    responses:
      200:
        description: Order status updated to delivered successfully
    """
    return update_order_status(order_id)
