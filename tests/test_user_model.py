import unittest
from app.models.user_model import User, users

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        # Clear the users list before each test
        users.clear()

    def tearDown(self):
        # Ensure users list is cleared after each test to maintain data isolation
        users.clear()

    def test_user_creation(self):
        user = User(
            username="testuser",
            email="testuser@example.com",
            password="password",  # Assuming plain text for testing, ideally hashed
            role="user",
            phone="1234567890",
            delivery_address="123 Test St",
            payment_info="Test Payment Info"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.password, "password")  # Replace with a hash check if hashed
        self.assertEqual(user.role, "user")
        self.assertEqual(user.phone, "1234567890")
        self.assertEqual(user.delivery_address, "123 Test St")
        self.assertEqual(user.payment_info, "Test Payment Info")

    def test_update_user_details(self):
        user = User(
            username="testuser",
            email="testuser@example.com",
            password="password",
            role="user",
            phone="1234567890",
            delivery_address="123 Test St",
            payment_info="Test Payment Info"
        )
        user.update_details(
            email="newemail@example.com",
            phone="0987654321",
            delivery_address="456 New St",
            payment_info="New Payment Info"
        )
        self.assertEqual(user.email, "newemail@example.com")
        self.assertEqual(user.phone, "0987654321")
        self.assertEqual(user.delivery_address, "456 New St")
        self.assertEqual(user.payment_info, "New Payment Info")

    def test_users_list(self):
        user1 = User(
            username="user1",
            email="user1@example.com",
            password="password1",
            role="user",
            phone="1234567890",
            delivery_address="123 Test St",
            payment_info="Payment Info 1"
        )
        user2 = User(
            username="user2",
            email="user2@example.com",
            password="password2",
            role="user",
            phone="0987654321",
            delivery_address="456 Test St",
            payment_info="Payment Info 2"
        )
        users.append(user1)
        users.append(user2)
        self.assertIn(user1, users)
        self.assertIn(user2, users)
        self.assertEqual(len(users), 2)

    def test_user_creation_without_optional_fields(self):
        user = User(
            username="testuser",
            email="testuser@example.com",
            password="password",
            role="user"
            # No phone, delivery_address, or payment_info
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.role, "user")
        self.assertIsNone(user.phone)
        self.assertIsNone(user.delivery_address)
        self.assertIsNone(user.payment_info)

if __name__ == '__main__':
    unittest.main()
