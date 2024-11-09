from flask import Flask
from flasgger import Swagger
from app.routes.user_routes import user_bp
from app.routes.order_routes import order_bp
from app.routes.restaurant_routes import restaurant_bp
from app.middlewares.error_middleware import handle_error

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    swagger = Swagger(app)
    # Register error handlers
    app.register_error_handler(Exception, handle_error)

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(restaurant_bp, url_prefix='/api/restaurants')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)