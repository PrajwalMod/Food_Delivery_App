from flask import Blueprint
from app.controllers.user_controller import register_user, get_user, update_user
from app.middlewares.auth_middleware import token_required

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user_route():
    return register_user()

@user_bp.route('/<user_id>', methods=['GET'])
@token_required
def get_user_route(user_id):
    return get_user(user_id)

@user_bp.route('/<user_id>', methods=['PUT'])
@token_required
def update_user_route(user_id):
    return update_user(user_id)
