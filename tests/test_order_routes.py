import unittest
from app import create_app
from flask import json
from app.utils.jwt_utils import generate_jwt


class OrderRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Register a user and obtain a token for authorization in certain tests
        self.client.post('/api/users/register', data=json.dumps({
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
            "role": "user"
        }), content_type='application/json')
        self.token = generate_jwt("testuser", "user")

    def tearDown(self):
        self.app_context.pop()

    def test_create_order_route(self):
        response = self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json', headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Order created successfully', str(response.data))

    def test_get_order_route(self):
        create_response = self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json', headers={"Authorization": f"Bearer {self.token}"})
        order_id = json.loads(create_response.data)['order_id']

        response = self.client.get(f'/api/orders/{order_id}', headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', str(response.data))

    def test_get_user_order_status_route(self):
        self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json', headers={"Authorization": f"Bearer {self.token}"})

        response = self.client.get('/api/orders/user/testuser/status',
                                   headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Pending', str(response.data))

    def test_update_order_status_route(self):
        # Register a restaurant owner and obtain a token
        self.client.post('/api/users/register', data=json.dumps({
            "username": "owneruser",
            "email": "owneruser@example.com",
            "password": "password",
            "role": "restaurant owner"
        }), content_type='application/json')
        owner_token = generate_jwt("owneruser", "restaurant owner")

        create_response = self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json', headers={"Authorization": f"Bearer {self.token}"})
        order_id = json.loads(create_response.data)['order_id']

        response = self.client.put(f'/api/orders/{order_id}/status', data=json.dumps({
            "status": "Accepted"
        }), content_type='application/json', headers={"Authorization": f"Bearer {owner_token}"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Order accepted successfully', str(response.data))

    def test_invalid_order_id(self):
        response = self.client.get('/api/orders/invalid_order_id', headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, 404)
        self.assertIn('Order not found', str(response.data))

    def test_unauthorized_access(self):
        create_response = self.client.post('/api/orders/', data=json.dumps({
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }), content_type='application/json', headers={"Authorization": f"Bearer {self.token}"})
        order_id = json.loads(create_response.data)['order_id']

        # Access without token
        response = self.client.put(f'/api/orders/{order_id}/status', data=json.dumps({
            "status": "Accepted"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Unauthorized', str(response.data))


if __name__ == '__main__':
    unittest.main()
