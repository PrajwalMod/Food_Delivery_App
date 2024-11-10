from app.models.order_model import Order, orders

def create_order(data):
    """
    Create a new order.

    Args:
        data (dict): A dictionary containing order details.

    Returns:
        Order: The created order object.
    """
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
    return next((o for o in orders if o.id == order_id), None)
