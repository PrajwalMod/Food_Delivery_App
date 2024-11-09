from flask import Flask, render_template_string
from flasgger import Swagger
from app.routes.user_routes import user_bp
from app.routes.order_routes import order_bp
from app.routes.restaurant_routes import restaurant_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    swagger = Swagger(app)

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(restaurant_bp, url_prefix='/api/restaurants')

    @app.route('/')
    def home():
        return render_template_string('<h1>Welcome to the App!</h1><p>The app is running.</p>')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
