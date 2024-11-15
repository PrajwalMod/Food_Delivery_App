from app import create_app
from flask_migrate import upgrade

app = create_app()

# Run migrations on app startup (not recommended for production)
with app.app_context():
    upgrade()

if __name__ == '__main__':
    app.run(debug=True)
