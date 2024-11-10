from app.models.user_model import User, users

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

def authenticate_user(username, password):
    """
    Authenticate a user.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        str: The JWT token if authentication is successful, else None.
    """
    users_collection = db['users']
    user = users_collection.find_one({'username': username})
    if user and sha256.verify(password, user['password']):
        token = encode_jwt({'username': username})
        return token
    return None