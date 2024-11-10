from functools import wraps
from flask import request, jsonify
from app.auth import decode_jwt

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
            try:
                token = token.split()[1]
            except IndexError:
                return jsonify({"message": "Token is invalid!"}), 403
            decoded = decode_jwt(token)
            if not decoded or decoded.get('role') != required_role:
                return jsonify({"message": "Access forbidden: insufficient permissions"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator
