from functools import wraps
from flask import request, jsonify
from app.models.user_model import users

def role_required(required_role):
    """
    Middleware to check for the required role in the request headers.

    Args:
        required_role (str): The role required to access the endpoint.

    Returns:
        function: The wrapped function that checks for the role.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({"message": "Token is missing!"}), 403
            # Here you would decode the token and get the user's role
            # For simplicity, let's assume the token is the username
            user = next((u for u in users if u.username == token), None)
            if not user or user.role != required_role:
                return jsonify({"message": "Access forbidden: insufficient permissions"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator
