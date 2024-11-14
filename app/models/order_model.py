from app.database import db
from uuid import uuid4

orders = []
class Order(db.Model):
    """
    A class to represent an order.

    Attributes:
        user_id (str): The ID of the user who placed the order.
        restaurant_id (str): The ID of the restaurant where the order was placed.
        items (list): A list of items in the order.
        total_price (float): The total price of the order.
        status (str): The status of the order.
    """

    __tablename__ = 'orders'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    user_id = db.Column(db.String, nullable=False)
    restaurant_id = db.Column(db.String, nullable=False)
    items = db.Column(db.PickleType, nullable=False)  # PickleType to store list data
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default="Pending")

    def __init__(self, user_id, restaurant_id, items, total_price):
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.items = items
        self.total_price = total_price
        self.status = "Pending"

    def update_status(self, status):
        """Update the order status."""
        self.status = status
