import unittest
from app import create_app
from flask import json
from app.utils.jwt_utils import generate_jwt
from app.database import db  # Ensure the test has access to the database session


class OrderControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize the app and testing context
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Setup test database (optional but recommended)
        db.create_all()

    def tearDown(self):
        # Cleanup database session to avoid side effects
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_order(self):
        # Register a user for the test order
        response = self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)  # Check user creation

        # Create an order
        response = self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn('Order created successfully', str(response.data))

    def test_get_order(self):
        # Register and create an order as in previous test
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')

        create_response = self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json')

        # Check order creation and retrieve order ID
        self.assertEqual(create_response.status_code, 201)
        order_id = json.loads(create_response.data).get('order_id')
        self.assertIsNotNone(order_id)  # Ensure order_id was created

        # Retrieve the order
        response = self.client.get(f'/api/orders/{order_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', str(response.data))

    def test_update_order_status(self):
        # Register user and create order as in previous tests
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "restaurant owner"
        }), content_type='application/json')

        create_response = self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json')

        order_id = json.loads(create_response.data).get('order_id')
        self.assertIsNotNone(order_id)

        # Generate authorization token for updating order
        token = generate_jwt("testuser", "restaurant owner")

        # Update order status
        response = self.client.put(f'/api/orders/{order_id}/status', data=json.dumps({
            "status": "Accepted"
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(response.status_code, 200)
        self.assertIn('Order accepted successfully', str(response.data))

    def test_get_user_order_status(self):
        # Register user and create order as in previous tests
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')

        self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json')

        # Check order status retrieval
        response = self.client.get('/api/orders/user/testuser/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Pending', str(response.data))


if __name__ == '__main__':
    unittest.main()
