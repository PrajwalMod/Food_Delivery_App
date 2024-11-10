import unittest
from app import create_app
from flask import json

class OrderControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_create_order(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password"
        }), content_type='application/json')
        response = self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Order created successfully', str(response.data))

    def test_get_order(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password"
        }), content_type='application/json')
        self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json')
        response = self.client.get('/api/orders/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', str(response.data))

    def test_update_order_status(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password"
        }), content_type='application/json')
        self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json')
        response = self.client.put('/api/orders/testuser/status', data=json.dumps({
            "status": "Accepted"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Order status updated successfully', str(response.data))

if __name__ == '__main__':
    unittest.main()
