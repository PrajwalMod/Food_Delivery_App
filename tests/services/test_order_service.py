import unittest
from app.services.order_service import create_order, get_order_by_id
from app.models.order_model import orders

class OrderServiceTestCase(unittest.TestCase):
    def setUp(self):
        # Clear the orders list before each test
        orders.clear()

    def test_create_order(self):
        data = {
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }
        order = create_order(data)
        self.assertEqual(order.user_id, "testuser")
        self.assertEqual(order.restaurant_id, "testrestaurant")
        self.assertEqual(order.items, ["item1", "item2"])
        self.assertEqual(order.total_price, 100.0)
        self.assertEqual(order.status, "Pending")
        self.assertIn(order, orders)

    def test_get_order_by_id(self):
        data = {
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }
        created_order = create_order(data)
        fetched_order = get_order_by_id(created_order.id)
        self.assertIsNotNone(fetched_order)
        self.assertEqual(fetched_order.user_id, "testuser")
        self.assertEqual(fetched_order.restaurant_id, "testrestaurant")
        self.assertEqual(fetched_order.items, ["item1", "item2"])
        self.assertEqual(fetched_order.total_price, 100.0)
        self.assertEqual(fetched_order.status, "Pending")

    def test_get_order_by_id_not_found(self):
        fetched_order = get_order_by_id("nonexistent_id")
        self.assertIsNone(fetched_order)

if __name__ == '__main__':
    unittest.main()