from flask import jsonify

def handle_error(e):
    """
    Middleware to handle errors and return a JSON response.

    Args:
        e (Exception): The exception that was raised.

    Returns:
        Response: JSON response with the error message.
    """
    response = jsonify({"message": str(e)})
    response.status_code = 500
    return response
