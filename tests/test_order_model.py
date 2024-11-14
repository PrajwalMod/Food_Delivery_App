import unittest
from app.models.order_model import Order, orders

class OrderModelTestCase(unittest.TestCase):
    def setUp(self):
        # Clear the orders list before each test
        orders.clear()

    def tearDown(self):
        # Clear orders after each test to ensure isolation
        orders.clear()

    def test_order_creation(self):
        order = Order(
            user_id="testuser",
            restaurant_id="testrestaurant",
            items=["item1", "item2"],
            total_price=100.0
        )
        self.assertEqual(order.user_id, "testuser")
        self.assertEqual(order.restaurant_id, "testrestaurant")
        self.assertEqual(order.items, ["item1", "item2"])
        self.assertEqual(order.total_price, 100.0)
        self.assertEqual(order.status, "Pending")
        self.assertIsNotNone(order.id)  # Ensure ID is assigned on creation

    def test_update_order_status(self):
        order = Order(
            user_id="testuser",
            restaurant_id="testrestaurant",
            items=["item1", "item2"],
            total_price=100.0
        )
        order.update_status("Accepted")
        self.assertEqual(order.status, "Accepted")

    def test_orders_list(self):
        order1 = Order(
            user_id="testuser1",
            restaurant_id="testrestaurant1",
            items=["item1", "item2"],
            total_price=100.0
        )
        order2 = Order(
            user_id="testuser2",
            restaurant_id="testrestaurant2",
            items=["item3", "item4"],
            total_price=200.0
        )
        orders.append(order1)
        orders.append(order2)
        self.assertIn(order1, orders)
        self.assertIn(order2, orders)
        self.assertEqual(len(orders), 2)

    def test_unique_order_ids(self):
        order1 = Order(
            user_id="testuser1",
            restaurant_id="testrestaurant1",
            items=["item1", "item2"],
            total_price=100.0
        )
        order2 = Order(
            user_id="testuser2",
            restaurant_id="testrestaurant2",
            items=["item3", "item4"],
            total_price=200.0
        )
        self.assertNotEqual(order1.id, order2.id, "Order IDs should be unique")

if __name__ == '__main__':
    unittest.main()
