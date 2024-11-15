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
        self.assertEqual(len(orders), 1)  # Ensure one order is added

    def test_create_multiple_orders(self):
        data1 = {
            "user_id": "user1",
            "restaurant_id": "restaurant1",
            "items": ["item1", "item2"],
            "total_price": 50.0
        }
        data2 = {
            "user_id": "user2",
            "restaurant_id": "restaurant2",
            "items": ["item3", "item4"],
            "total_price": 75.0
        }
        order1 = create_order(data1)
        order2 = create_order(data2)
        self.assertNotEqual(order1.id, order2.id)  # Check that IDs are unique
        self.assertEqual(len(orders), 2)

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

    def test_order_list_integrity(self):
        data = {
            "user_id": "testuser",
            "restaurant_id": "testrestaurant",
            "items": ["item1", "item2"],
            "total_price": 100.0
        }
        create_order(data)
        create_order(data)  # Add another order with same data
        self.assertEqual(len(orders), 2)  # Ensure both orders are in the list

if __name__ == '__main__':
    unittest.main()
