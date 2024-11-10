from functools import wraps
from flask import request, jsonify
from app.auth import decode_jwt

def token_required(f):
    """
    Middleware to check for a valid token in the request headers.

    Args:
        f (function): The route handler function.

    Returns:
        function: The wrapped function that checks for the token.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 403
        try:
            token = token.split()[1]
        except IndexError:
            return jsonify({"message": "Token is invalid!"}), 403
        decoded = decode_jwt(token)
        if not decoded:
            return jsonify({"message": "Token is invalid!"}), 403
        return f(*args, **kwargs)
    return decorated
