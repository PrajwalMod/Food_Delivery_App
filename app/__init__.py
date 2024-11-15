from flask import Flask, render_template_string
from flasgger import Swagger
from pymongo import MongoClient
from app.routes.user_routes import user_bp
from app.routes.order_routes import order_bp
from app.routes.restaurant_routes import restaurant_bp

from flask_migrate import Migrate
from app.database import db
import os
from flask_cors import CORS

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", os.urandom(24))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/food_delivery_db' # for local
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(restaurant_bp, url_prefix='/api/restaurants')

    # Initialize database and Swagger
    Swagger(app)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def home():
        return render_template_string('<h1>Welcome to the App!</h1><p>The app is running.</p>')

    return app