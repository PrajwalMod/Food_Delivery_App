class User:
    """
    A class to represent a user.

    Attributes:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        role (str): The role of the user (e.g., 'admin', 'user', 'restaurant owner', 'delivery agent').
        phone (str): The phone number of the user.
        delivery_address (str): The delivery address of the user.
        payment_info (str): The payment information of the user.
    """
    def __init__(self, username, email, password, role='user', phone=None, delivery_address=None, payment_info=None):
        """
        Constructs all the necessary attributes for the user object.

        Args:
            username (str): The username of the user.
            email (str): The email of the user.
            password (str): The password of the user.
            role (str): The role of the user.
            phone (str): The phone number of the user.
            delivery_address (str): The delivery address of the user.
            payment_info (str): The payment information of the user.
        """
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.phone = phone
        self.delivery_address = delivery_address
        self.payment_info = payment_info

    def update_details(self, email=None, phone=None, delivery_address=None, payment_info=None):
        """
        Update the user details.

        Args:
            email (str): The new email of the user.
            phone (str): The new phone number of the user.
            delivery_address (str): The new delivery address of the user.
            payment_info (str): The new payment information of the user.
        """
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if delivery_address:
            self.delivery_address = delivery_address
        if payment_info:
            self.payment_info = payment_info

# Define a list to store user objects
users = []
