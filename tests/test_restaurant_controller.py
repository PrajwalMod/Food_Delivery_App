import unittest
from app import create_app
from flask import json
from app.utils.jwt_utils import generate_jwt
from app.database import db  # Ensure database session is accessible in tests


class RestaurantControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize the app and setup database context
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create tables for the test database
        db.create_all()

    def tearDown(self):
        # Clean up database after each test to avoid side effects
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_restaurant(self):
        # Register a user as a restaurant owner and authenticate
        response = self.client.post('/api/users/register', data=json.dumps({
            "username": "owner",
            "email": "owner@example.com",
            "password": "password",
            "role": "restaurant owner"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)  # Ensure user registration was successful

        token = generate_jwt("owner", "restaurant owner")

        # Add a restaurant
        response = self.client.post('/api/restaurants/', data=json.dumps({
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            "work_hours": "9 AM - 9 PM"
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(response.status_code, 201)
        self.assertIn('Restaurant added successfully', str(response.data))

    def test_get_restaurant(self):
        # Register user, create restaurant, and retrieve its details
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

        # Retrieve the created restaurant
        response = self.client.get('/api/restaurants/Test Restaurant')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Restaurant', str(response.data))

    def test_update_restaurant(self):
        # Register user, add restaurant, and update its details
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

        # Update restaurant details
        response = self.client.put('/api/restaurants/Test Restaurant', data=json.dumps({
            "address": "123 New St",
            "cuisine": "New Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0},
                     {"name": "item3", "price": 20.0}],
            "work_hours": "10 AM - 10 PM"
        }), content_type='application/json', headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(response.status_code, 200)
        self.assertIn('Restaurant details updated successfully', str(response.data))

    def test_search_restaurants(self):
        # Register user, add restaurant, and perform search by cuisine
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

        # Search for the restaurant by cuisine
        response = self.client.get('/api/restaurants/search?cuisine=Test Cuisine')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Restaurant', str(response.data))


if __name__ == '__main__':
    unittest.main()
