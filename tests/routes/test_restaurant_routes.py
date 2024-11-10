import unittest
from app import create_app
from flask import json
from app.utils.jwt_utils import generate_jwt

class RestaurantRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_add_restaurant_route(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "owner",
            "email": "owner@example.com",
            "password": "password",
            "role": "restaurant owner"
        }), content_type='application/json')
        token = generate_jwt("owner", "restaurant owner")
        response = self.client.post('/api/restaurants/', data=json.dumps({
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            "work_hours": "9 AM - 9 PM"
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Restaurant added successfully', str(response.data))

    def test_get_restaurant_route(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "owner",
            "email": "owner@example.com",
            "password": "password",
            "role": "restaurant owner"
        }), content_type='application/json')
        token = generate_jwt("owner", "restaurant owner")
        self.client.post('/api/restaurants/', data=json.dumps({
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            "work_hours": "9 AM - 9 PM"
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})
        response = self.client.get('/api/restaurants/Test Restaurant')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Restaurant', str(response.data))

    def test_update_restaurant_route(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "owner",
            "email": "owner@example.com",
            "password": "password",
            "role": "restaurant owner"
        }), content_type='application/json')
        token = generate_jwt("owner", "restaurant owner")
        self.client.post('/api/restaurants/', data=json.dumps({
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            "work_hours": "9 AM - 9 PM"
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})
        response = self.client.put('/api/restaurants/Test Restaurant', data=json.dumps({
            "address": "123 New St",
            "cuisine": "New Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}, {"name": "item3", "price": 20.0}],
            "work_hours": "10 AM - 10 PM"
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Restaurant details updated successfully', str(response.data))

    def test_search_restaurants_route(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "owner",
            "email": "owner@example.com",
            "password": "password",
            "role": "restaurant owner"
        }), content_type='application/json')
        token = generate_jwt("owner", "restaurant owner")
        self.client.post('/api/restaurants/', data=json.dumps({
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            "work_hours": "9 AM - 9 PM"
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})
        response = self.client.get('/api/restaurants/search?cuisine=Test Cuisine')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Restaurant', str(response.data))

    def test_update_order_status_route(self):
        self.client.post('/api/users/register', data=json.dumps({
            "username": "owner",
            "email": "owner@example.com",
            "password": "password",
            "role": "restaurant owner"
        }), content_type='application/json')
        token = generate_jwt("owner", "restaurant owner")
        create_response = self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "Test Restaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})
        order_id = json.loads(create_response.data)['order_id']
        response = self.client.put(f'/api/orders/{order_id}/status', data=json.dumps({
            "status": "Accepted"
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Order accepted successfully', str(response.data))

if __name__ == '__main__':
    unittest.main()