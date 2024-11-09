from flask import Blueprint
from app.controllers.order_controller import (
    create_order, get_order, get_user_order_status, update_order_status
)
from app.middlewares.auth_middleware import token_required
from app.middlewares.role_middleware import role_required

order_bp = Blueprint('orders', __name__)

@order_bp.route('/', methods=['POST'])
@token_required
def create_order_route():
    return create_order()

@order_bp.route('/<order_id>', methods=['GET'])
@token_required
def get_order_route(order_id):
    return get_order(order_id)

@order_bp.route('/user/<user_id>/status', methods=['GET'])
@token_required
def get_user_orders_route(user_id):
    return get_user_order_status(user_id)

@order_bp.route('/<order_id>/status', methods=['PUT'])
@token_required
@role_required('restaurant_owner')
def update_status_route(order_id):
    return update_order_status(order_id)

@order_bp.route('/<order_id>/pickup', methods=['PUT'])
@token_required
@role_required('delivery_agent')
def pickup_route(order_id):
    return update_order_status(order_id)

@order_bp.route('/<order_id>/deliver', methods=['PUT'])
@token_required
@role_required('delivery_agent')
def deliver_route(order_id):
    return update_order_status(order_id)
