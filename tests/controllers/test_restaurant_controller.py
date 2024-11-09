import unittest
from app import create_app
from flask import json

class RestaurantControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_add_restaurant(self):
        response = self.client.post('/api/restaurants/', data=json.dumps({
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": ["item1", "item2"]
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Restaurant added successfully', str(response.data))

    def test_get_restaurant(self):
        self.client.post('/api/restaurants/', data=json.dumps({
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": ["item1", "item2"]
        }), content_type='application/json')
        response = self.client.get('/api/restaurants/Test Restaurant')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Restaurant', str(response.data))

if __name__ == '__main__':
    unittest.main()
