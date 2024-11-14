from flask import request, jsonify
from app.models.user_model import User
from app.database import db


def register_user():
    """
    Register a new user.

    Returns:
        Response: JSON response with a success message or error.
    """
    data = request.get_json()
    try:
        user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            role=data.get('role', 'user')  # Default role is 'user'
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error registering user: {str(e)}"}), 400


def get_user(user_id):
    """
    Get user profile.

    Args:
        user_id (str): The ID of the user.

    Returns:
        Response: JSON response with user details or an error message.
    """
    user = User.query.get(user_id)
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "phone": user.phone,
            "delivery_address": user.delivery_address,
            "payment_info": user.payment_info
        }), 200
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
    user = User.query.get(user_id)
    if user:
        try:
            user.update_details(
                email=data.get('email'),
                phone=data.get('phone'),
                delivery_address=data.get('delivery_address'),
                payment_info=data.get('payment_info')
            )
            db.session.commit()
            return jsonify({"message": "User details updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": f"Error updating user: {str(e)}"}), 400
    return jsonify({"message": "User not found"}), 404
