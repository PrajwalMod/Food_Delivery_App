import re

def validate_email(email):
    """
    Validate the email format.

    Args:
        email (str): The email to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """
    Validate the password strength.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is strong, False otherwise.
    """
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True
