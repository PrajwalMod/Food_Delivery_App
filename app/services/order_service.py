from app.models.order_model import Order, orders

def create_order(data):
    """
    Create a new order.

    Args:
        data (dict): A dictionary containing order details.

    Returns:
        Order: The created order object or raises an exception if invalid data is provided.
    """
    # Ensure required fields are provided in the data
    required_fields = ['user_id', 'restaurant_id', 'items', 'total_price']
    print(data)
    if not all(field in data for field in required_fields):
        raise ValueError("Missing required fields: user_id, restaurant_id, items, total_price")

    order = Order(**data)
    orders.append(order)
    return order

def get_order_by_id(order_id):
    """
    Get an order by its ID.

    Args:
        order_id (str): The ID of the order.

    Returns:
        Order: The order object if found, else None.
    """
    order = next((o for o in orders if o.id == order_id), None)
    if not order:
        raise ValueError(f"Order with ID {order_id} not found")
    return order
