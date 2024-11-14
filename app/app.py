# from flask import Flask, render_template_string
# from flasgger import Swagger
# from app.database import db
# from app.routes.user_routes import user_bp
# from app.routes.order_routes import order_bp
# from app.routes.restaurant_routes import restaurant_bp
#
# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'your_secret_key'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/food_delivery_db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#     # Initialize database and Swagger
#     db.init_app(app)
#     Swagger(app)
#
#     # Register blueprints
#     app.register_blueprint(user_bp, url_prefix='/api/users')
#     app.register_blueprint(order_bp, url_prefix='/api/orders')
#     app.register_blueprint(restaurant_bp, url_prefix='/api/restaurants')
#
#     # Create tables within the app context
#     with app.app_context():
#         db.create_all()
#
#     # Define a simple home route
#     @app.route('/')
#     def home():
#         return render_template_string('<h1>Welcome to the App!</h1><p>The app is running.</p>')
#
#     return app
#
# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)
