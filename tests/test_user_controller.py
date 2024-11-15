import unittest
from app import create_app
from flask import json
from app.database import db  # Ensure database context is accessible


class UserControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Initialize the test database tables
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_user(self):
        # Test user registration
        response = self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'User registered successfully')

    def test_login_user(self):
        # Register the user first to ensure they can log in
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')

        # Test login with valid credentials
        response = self.client.post('/api/users/login', data=json.dumps({
            "username": "testuser",
            "password": "password"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn('token', json_data)  # Ensure a token is present

    def test_login_user_invalid_credentials(self):
        # Register the user first to set up the test case
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')

        # Attempt login with invalid credentials
        response = self.client.post('/api/users/login', data=json.dumps({
            "username": "testuser",
            "password": "wrongpassword"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 401)
        json_data = response.get_json()
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Invalid credentials')


if __name__ == '__main__':
    unittest.main()
