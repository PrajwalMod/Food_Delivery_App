from app.models.user_model import User, users
from flask import current_app
from app.utils.jwt_utils import generate_jwt
from werkzeug.security import check_password_hash, generate_password_hash

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
    return next((u for u in users if u.username == user_id), None)

def get_db():
    return current_app.config['DATABASE']

def register_user(data):
    db = get_db()
    users_collection = db['users']
    if users_collection.find_one({"username": data['username']}):
        return {"message": "User already exists"}, 400
    hashed_password = generate_password_hash(data['password'])
    user = {
        "username": data['username'],
        "email": data['email'],
        "password": hashed_password,
        "role": data.get('role', 'user')
    }
    users_collection.insert_one(user)
    print(f"Registered user: {user}")  # Print the registered user details
    return {"message": "User registered successfully"}, 201

def authenticate_user(username, password):
    db = get_db()
    users_collection = db['users']
    user = users_collection.find_one({"username": username})
    print(f"Authenticating user: {user}")  # Print the user details being authenticated
    if user and check_password_hash(user['password'], password):
        token = generate_jwt(user['username'], user['role'])
        return token
    return None
