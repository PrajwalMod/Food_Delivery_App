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
