class Order:
    """
    A class to represent an order.

    Attributes:
        order_id (str): The unique identifier for the order.
        user_id (str): The ID of the user who placed the order.
        restaurant_id (str): The ID of the restaurant where the order was placed.
        items (list): A list of items in the order.
        total_price (float): The total price of the order.
        status (str): The status of the order.
    """

    def __init__(self, order_id, user_id, restaurant_id, items, total_price, status="Pending"):
        """
        Constructs all the necessary attributes for the order object.
        Args:
            order_id (str): The unique identifier for the order.
            user_id (str): The ID of the user who placed the order.
            restaurant_id (str): The ID of the restaurant where the order was placed.
            items (list): A list of items in the order.
            total_price (float): The total price of the order.
            status (str, optional): The status of the order. Defaults to "Pending".
        """
        self.order_id = order_id
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.items = items
        self.total_price = total_price
        self.status = status

    def update_status(self, new_status):
        """
        Update the order status.

        Args:
            new_status (str): The new status of the order.

        Returns:
            bool: True if the status was updated successfully, False otherwise.
        """
        valid_statuses = ['Pending', 'Accepted', 'Rejected', 'Picked Up', 'Delivered']
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False
# In-memory storage
orders = []
