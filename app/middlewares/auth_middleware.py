from functools import wraps
from flask import request, jsonify

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
        # Add token verification logic here
        return f(*args, **kwargs)
    return decorated
