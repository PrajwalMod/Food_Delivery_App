from flask import request, jsonify
from app.models.user_model import User, users

def register_user():
    """
    Register a new user.
    Returns:
        Response: JSON response with a success message.
    """
    data = request.get_json()
    role = data.get('role', 'user')  # Default role is 'user'
    user = User(username=data['username'], email=data['email'], password=data['password'], role=role)
    users.append(user)
    return jsonify({"message": "User registered successfully"}), 201

def get_user(user_id):
    """
    Get user profile.
    Args:
        user_id (str): The ID of the user.
    Returns:
        Response: JSON response with user details or an error message.
    """
    user = next((u for u in users if u.username == user_id), None)
    if user:
        return jsonify(user.__dict__), 200
    return jsonify({"message": "User not found"}), 404

def update_user(user_id):
    """
    Update user details.
    Args:
        user_id (str): The ID of the user.
    Returns:
        Response: JSON response with a success message or an error message.
    """
    data = request.get_json()
    user = next((u for u in users if u.username == user_id), None)
    if user:
        user.update_details(**data)
        return jsonify({"message": "User details updated successfully"}), 200
    return jsonify({"message": "User not found"}), 404
