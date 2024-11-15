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
        # Register the user
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')

        # Authenticate the user
        token = authenticate_user("testuser", "password")
        self.assertIsNotNone(token)

        # Optional: Verify token structure, e.g., checking role in token payload
        decoded_token = json.loads(token)
        self.assertEqual(decoded_token.get("username"), "testuser")
        self.assertEqual(decoded_token.get("role"), "user")

    def test_authenticate_user_invalid_credentials(self):
        # Register the user
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')

        # Attempt to authenticate with an incorrect password
        token = authenticate_user("testuser", "wrongpassword")
        self.assertIsNone(token)

    def test_authenticate_unregistered_user(self):
        # Attempt to authenticate without registering
        token = authenticate_user("unregistereduser", "password")
        self.assertIsNone(token)

    def test_authenticate_case_sensitivity(self):
        # Register the user with specific case
        self.client.post('/api/users/register', data=json.dumps({
            "username": "CaseSensitiveUser",
            "email": "caseuser@example.com",
            "password": "CasePassword",
            "role": "user"
        }), content_type='application/json')

        # Attempt to authenticate with incorrect case
        token = authenticate_user("casesensitiveuser", "casepassword")
        self.assertIsNone(token)  # Should fail if authentication is case-sensitive


if __name__ == '__main__':
    unittest.main()
