# This file can be left empty or used to initialize the app packagefrom app.routes.user_routes import user_bp
from app.routes.order_routes import order_bp
from app.routes.restaurant_routes import restaurant_bp

__all__ = ['user_bp', 'order_bp', 'restaurant_bp']
