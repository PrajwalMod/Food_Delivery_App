from flask import Blueprint, request, jsonify
from app.controllers.restaurant_controller import add_restaurant, get_restaurant, update_restaurant, search_restaurants, update_order_status
from app.middlewares.role_middleware import role_required

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/', methods=['POST'])
@role_required('restaurant owner')
def add_restaurant_route():
    """
    Add a new restaurant
    ---
    tags:
      - Restaurants
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - name
            - address
            - cuisine
            - menu
            - work_hours
          properties:
            name:
              type: string
            address:
              type: string
            cuisine:
              type: string
            menu:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                  price:
                    type: number
            work_hours:
              type: string
    responses:
      201:
        description: Restaurant added successfully
    """
    return add_restaurant()

@restaurant_bp.route('/<restaurant_id>', methods=['GET'])
def get_restaurant_route(restaurant_id):
    """
    Get restaurant details
    ---
    tags:
      - Restaurants
    parameters:
      - in: path
        name: restaurant_id
        type: string
        required: true
    responses:
      200:
        description: Restaurant details retrieved successfully
    """
    return get_restaurant(restaurant_id)

@restaurant_bp.route('/<restaurant_id>', methods=['PUT'])
@role_required('restaurant owner')
def update_restaurant_route(restaurant_id):
    """
    Update restaurant details
    ---
    tags:
      - Restaurants
    parameters:
      - in: path
        name: restaurant_id
        type: string
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            address:
              type: string
            cuisine:
              type: string
            menu:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                  price:
                    type: number
            work_hours:
              type: string
    responses:
      200:
        description: Restaurant details updated successfully
    """
    return update_restaurant(restaurant_id)

@restaurant_bp.route('/search', methods=['GET'])
def search_restaurants_route():
    """
    Search for restaurants
    ---
    tags:
      - Restaurants
    parameters:
      - in: query
        name: cuisine
        type: string
        required: false
      - in: query
        name: max_price
        type: number
        required: false
    responses:
      200:
        description: List of matching restaurants
    """
    return search_restaurants()

@restaurant_bp.route('/orders/<order_id>', methods=['PUT'])
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
    responses:
      200:
        description: Order status updated successfully
    """
    return update_order_status(order_id)
