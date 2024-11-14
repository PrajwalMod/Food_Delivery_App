from app.database import db
from uuid import uuid4

users = []  # This should be your list or collection of users
class User(db.Model):
    """
    A class to represent a user.

    Attributes:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        role (str): The role of the user.
        phone (str): The phone number of the user.
        delivery_address (str): The delivery address of the user.
        payment_info (str): The payment information of the user.
    """

    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, default='user')
    phone = db.Column(db.String, nullable=True)
    delivery_address = db.Column(db.String, nullable=True)
    payment_info = db.Column(db.String, nullable=True)

    def __init__(self, username, email, password, role='user', phone=None, delivery_address=None, payment_info=None):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.phone = phone
        self.delivery_address = delivery_address
        self.payment_info = payment_info

    def update_details(self, email=None, phone=None, delivery_address=None, payment_info=None):
        """Update the user details."""
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if delivery_address:
            self.delivery_address = delivery_address
        if payment_info:
            self.payment_info = payment_info
