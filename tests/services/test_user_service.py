import unittest
from app.services.user_service import authenticate_user
from app import create_app
from flask import json

class UserServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_authenticate_user(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')
        token = authenticate_user("testuser", "password")
        self.assertIsNotNone(token)

    def test_authenticate_user_invalid_credentials(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')
        token = authenticate_user("testuser", "wrongpassword")
        self.assertIsNone(token)

if __name__ == '__main__':
    unittest.main()