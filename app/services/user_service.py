from app.models.user_model import User, users
from flask import current_app
from app.utils.jwt_utils import generate_jwt
from werkzeug.security import check_password_hash, generate_password_hash

import jwt
import datetime

# Secret key for signing the token
secret_key = "i6nneftv@r"

# Header and payload for the token
header = {"alg": "HS256", "typ": "JWT"}

def create_user(data):
    """
    Create a new user.

    Args:
        data (dict): A dictionary containing user details.

    Returns:
        User: The created user object.
    """
    user = User(**data)
    users.append(user)
    return user


def get_user_by_id(user_id):
    """
    Get a user by their ID.

    Args:
        user_id (str): The ID of the user.

    Returns:
        User: The user object if found, else None.
    """
    user = next((u for u in users if u.username == user_id), None)
    if not user:
        raise ValueError(f"User with ID {user_id} not found.")
    return user


def get_db():
    return current_app.config['DATABASE']


def register_user(data):
    """
    Register a new user in the database.

    Args:
        data (dict): A dictionary containing user registration details.

    Returns:
        dict: Response message and status code.
    """
    db = get_db()
    users_collection = db['users']

    # Check if the user already exists
    if users_collection.find_one({"username": data['username']}):
        return {"message": "User already exists"}, 400

    # Hash the password before saving
    hashed_password = generate_password_hash(data['password'])
    user = {
        "username": data['username'],
        "email": data['email'],
        "password": hashed_password,
        "role": data.get('role', 'user')
    }

    # Insert the new user
    users_collection.insert_one(user)
    return {"message": "User registered successfully"}, 201


def authenticate_user(username, password):
    """
    Authenticate a user.

    Args:
        username (str): The username of the user.
        password (str): The password entered by the user.

    Returns:
        str: A JWT token if authentication is successful, else None.
    """
    # db = get_db()
    # users_collection = db['users']

    payload = {
        "username": username,
        "password": password,
        "iat": datetime.datetime.now(),
        "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
    }

    # Encode the token
    token = jwt.encode(payload, secret_key, algorithm="HS256", headers=header)

    # # Find the user by username
    # user = users_collection.find_one({"username": username})
    #
    # if user and check_password_hash(user['password'], password):
    #     # Generate JWT token if user is authenticated
    #     token = generate_jwt(user['username'], user['role'])
    #     return token

    return token
