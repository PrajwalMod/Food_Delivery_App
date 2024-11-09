from app.models.order_model import Order, orders
from app.utils.exceptions import ValidationError, ResourceNotFoundError

class OrderService:
    @staticmethod
    def create_order(user_id, restaurant_id, items, total_price):
        order = Order(
            order_id=str(len(orders) + 1),  # Simple ID generation
            user_id=user_id,
            restaurant_id=restaurant_id,
            items=items,
            total_price=total_price
        )
        orders.append(order)
        return order

    @staticmethod
    def get_order(order_id):
        order = next((o for o in orders if o.order_id == order_id), None)
        if not order:
            raise ResourceNotFoundError("Order not found")
        return order

    @staticmethod
    def get_user_orders(user_id):
        user_orders = [order for order in orders if order.user_id == user_id]
        return user_orders

    @staticmethod
    def update_order_status(order_id, status, role):
        order = next((o for o in orders if o.order_id == order_id), None)
        if not order:
            raise ResourceNotFoundError("Order not found")

        valid_statuses = {
            'restaurant_owner': ['Accepted', 'Rejected'],
            'delivery_agent': ['Picked Up', 'Delivered'],
            'user': []
        }

        if status not in valid_statuses.get(role, []):
            raise ValidationError("Invalid status update for this role")

        order.update_status(status)
        return order