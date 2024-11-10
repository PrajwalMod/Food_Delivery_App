from flask import Blueprint, request, jsonify
from app.controllers.user_controller import register_user, get_user, update_user
from app.services.user_service import authenticate_user
from app.auth import decode_jwt

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user_route():
    """
    Register a new user
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - username
            - email
            - password
          properties:
            username:
              type: string
            email:
              type: string
            password:
              type: string
            role:
              type: string
    responses:
      201:
        description: User registered successfully
    """
    return register_user()

@user_bp.route('/login', methods=['POST'])
def login():
    """
    User login
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: User logged in successfully
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    token = authenticate_user(username, password)
    if token:
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@user_bp.route('/<user_id>', methods=['GET'])
def get_user_route(user_id):
    """
    Get user profile
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: user_id
        type: string
        required: true
    responses:
      200:
        description: User profile retrieved successfully
    """
    return get_user(user_id)

@user_bp.route('/<user_id>', methods=['PUT'])
def update_user_route(user_id):
    """
    Update user details
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: user_id
        type: string
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            email:
              type: string
            phone:
              type: string
            delivery_address:
              type: string
            payment_info:
              type: string
    responses:
      200:
        description: User details updated successfully
    """
    return update_user(user_id)
