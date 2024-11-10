import uuid

class Order:
    """
    A class to represent an order.

    Attributes:
        user_id (str): The ID of the user who placed the order.
        restaurant_id (str): The ID of the restaurant where the order was placed.
        items (list): A list of items in the order.
        total_price (float): The total price of the order.
        status (str): The status of the order.
    """

    def __init__(self, user_id, restaurant_id, items, total_price):
        """
        Constructs all the necessary attributes for the order object.

        Args:
            user_id (str): The ID of the user who placed the order.
            restaurant_id (str): The ID of the restaurant where the order was placed.
            items (list): A list of items in the order.
            total_price (float): The total price of the order.
        """
        self.id = str(uuid.uuid4())  # Ensure each order has a unique ID
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.items = items
        self.total_price = total_price
        self.status = "Pending"

    def update_status(self, status):
        """
        Update the order status.

        Args:
            status (str): The new status of the order.
        """
        self.status = status

# In-memory storage for simplicity
orders = []
