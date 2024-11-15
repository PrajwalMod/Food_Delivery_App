import unittest
from app import create_app
from flask import json


class UserRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_register_user_route(self):
        response = self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', str(response.data))

    def test_register_duplicate_user(self):
        # First registration
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')

        # Attempt duplicate registration
        response = self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('User already exists', str(response.data))

    def test_register_user_missing_fields(self):
        response = self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser"
            # Missing email and password fields
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required fields', str(response.data))

    def test_login_user_route(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')
        response = self.client.post('/api/users/login', data=json.dumps({
            "username": "testuser",
            "password": "password"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', str(response.data))

        # Check that the token is in valid format (optional)
        token = json.loads(response.data).get("token")
        self.assertIsNotNone(token)
        self.assertTrue(len(token) > 10)  # Example length check

    def test_login_user_invalid_credentials_route(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')
        response = self.client.post('/api/users/login', data=json.dumps({
            "username": "testuser",
            "password": "wrongpassword"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid credentials', str(response.data))

    def test_login_user_nonexistent_user(self):
        response = self.client.post('/api/users/login', data=json.dumps({
            "username": "nonexistent",
            "password": "password"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found', str(response.data))


if __name__ == '__main__':
    unittest.main()
