import jwt
import datetime
from flask import current_app

def encode_jwt(payload):
    """
    Encode a JWT token.

    Args:
        payload (dict): The payload to encode in the token.

    Returns:
        str: The encoded JWT token.
    """
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

def decode_jwt(token):
    """
    Decode a JWT token.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict: The decoded payload if the token is valid, else None.
    """
    try:
        return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None