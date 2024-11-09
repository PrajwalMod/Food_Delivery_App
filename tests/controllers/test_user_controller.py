import unittest
from app import create_app
from flask import json

class UserControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_register_user(self):
        response = self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', str(response.data))

    def test_get_user(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password"
        }), content_type='application/json')
        response = self.client.get('/api/users/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', str(response.data))

if __name__ == '__main__':
    unittest.main()
