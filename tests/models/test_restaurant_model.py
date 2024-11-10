import unittest
from app.models.restaurant_model import Restaurant, restaurants

class RestaurantModelTestCase(unittest.TestCase):
    def setUp(self):
        # Clear the restaurants list before each test
        restaurants.clear()

    def test_restaurant_creation(self):
        restaurant = Restaurant(
            name="Test Restaurant",
            address="123 Test St",
            cuisine="Test Cuisine",
            menu=[{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            work_hours="9 AM - 9 PM"
        )
        self.assertEqual(restaurant.name, "Test Restaurant")
        self.assertEqual(restaurant.address, "123 Test St")
        self.assertEqual(restaurant.cuisine, "Test Cuisine")
        self.assertEqual(restaurant.menu, [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}])
        self.assertEqual(restaurant.work_hours, "9 AM - 9 PM")

    def test_update_restaurant_details(self):
        restaurant = Restaurant(
            name="Test Restaurant",
            address="123 Test St",
            cuisine="Test Cuisine",
            menu=[{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            work_hours="9 AM - 9 PM"
        )
        restaurant.update_details(
            address="123 New St",
            cuisine="New Cuisine",
            menu=[{"name": "item1", "price": 12.0}, {"name": "item2", "price": 18.0}],
            work_hours="10 AM - 10 PM"
        )
        self.assertEqual(restaurant.address, "123 New St")
        self.assertEqual(restaurant.cuisine, "New Cuisine")
        self.assertEqual(restaurant.menu, [{"name": "item1", "price": 12.0}, {"name": "item2", "price": 18.0}])
        self.assertEqual(restaurant.work_hours, "10 AM - 10 PM")

    def test_restaurants_list(self):
        restaurant1 = Restaurant(
            name="Restaurant 1",
            address="Address 1",
            cuisine="Cuisine 1",
            menu=[{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            work_hours="9 AM - 9 PM"
        )
        restaurant2 = Restaurant(
            name="Restaurant 2",
            address="Address 2",
            cuisine="Cuisine 2",
            menu=[{"name": "item3", "price": 20.0}, {"name": "item4", "price": 25.0}],
            work_hours="10 AM - 10 PM"
        )
        restaurants.append(restaurant1)
        restaurants.append(restaurant2)
        self.assertIn(restaurant1, restaurants)
        self.assertIn(restaurant2, restaurants)
        self.assertEqual(len(restaurants), 2)

if __name__ == '__main__':
    unittest.main()