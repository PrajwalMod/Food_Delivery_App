import unittest
from app.services.restaurant_service import add_restaurant, get_restaurant_by_id
from app.models.restaurant_model import restaurants

class RestaurantServiceTestCase(unittest.TestCase):
    def setUp(self):
        # Clear the restaurants list before each test
        restaurants.clear()

    def test_add_restaurant(self):
        data = {
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            "work_hours": "9 AM - 9 PM"
        }
        restaurant = add_restaurant(data)
        self.assertEqual(restaurant.name, "Test Restaurant")
        self.assertEqual(restaurant.address, "123 Test St")
        self.assertEqual(restaurant.cuisine, "Test Cuisine")
        self.assertEqual(restaurant.menu, [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}])
        self.assertEqual(restaurant.work_hours, "9 AM - 9 PM")
        self.assertIn(restaurant, restaurants)
        self.assertEqual(len(restaurants), 1)  # Check that one restaurant is added

    def test_add_duplicate_restaurant_name(self):
        data = {
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            "work_hours": "9 AM - 9 PM"
        }
        add_restaurant(data)
        duplicate_restaurant = add_restaurant(data)
        self.assertIsNone(duplicate_restaurant)  # Assuming duplicate names aren't allowed
        self.assertEqual(len(restaurants), 1)  # Only one should exist in the list

    def test_get_restaurant_by_id(self):
        data = {
            "name": "Test Restaurant",
            "address": "123 Test St",
            "cuisine": "Test Cuisine",
            "menu": [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}],
            "work_hours": "9 AM - 9 PM"
        }
        created_restaurant = add_restaurant(data)
        fetched_restaurant = get_restaurant_by_id(created_restaurant.name)
        self.assertIsNotNone(fetched_restaurant)
        self.assertEqual(fetched_restaurant.name, "Test Restaurant")
        self.assertEqual(fetched_restaurant.address, "123 Test St")
        self.assertEqual(fetched_restaurant.cuisine, "Test Cuisine")
        self.assertEqual(fetched_restaurant.menu, [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 15.0}])
        self.assertEqual(fetched_restaurant.work_hours, "9 AM - 9 PM")

    def test_get_restaurant_by_id_not_found(self):
        fetched_restaurant = get_restaurant_by_id("nonexistent_id")
        self.assertIsNone(fetched_restaurant)

    def test_restaurant_list_integrity(self):
        data1 = {
            "name": "Restaurant One",
            "address": "123 Test St",
            "cuisine": "Italian",
            "menu": [{"name": "pizza", "price": 12.0}],
            "work_hours": "10 AM - 10 PM"
        }
        data2 = {
            "name": "Restaurant Two",
            "address": "456 Test Ave",
            "cuisine": "Mexican",
            "menu": [{"name": "taco", "price": 8.0}],
            "work_hours": "11 AM - 11 PM"
        }
        add_restaurant(data1)
        add_restaurant(data2)
        self.assertEqual(len(restaurants), 2)  # Both restaurants should be in the list

if __name__ == '__main__':
    unittest.main()
