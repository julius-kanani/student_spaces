import unittest
from models.user import User
from models.engine.db_storage import DBStorage

class TestUserModel(unittest.TestCase):
    def setUp(self):
        # Initialize DBStorage
        self.storage = DBStorage()
        self.storage.reload()

    def test_create_user(self):
        # Create a new user
        user_data = {
            'username': 'test_user',
            'password': 'test_password',
            'email': 'test@example.com',
            'full_name': 'Test User',
            'phone_number': '1234567890',
            'user_type': 'student',  # or 'landlord'
            'university_id': '1234'
            # Add other attributes as needed
        }
        new_user = User(**user_data)
        self.storage.new(new_user)
        self.storage.save()

        # Retrieve the user from the database
        retrieved_user = self.storage.get(User, new_user.id)

        # Check if the retrieved user matches the created user
        self.assertEqual(retrieved_user.username, user_data['username'])
        self.assertEqual(retrieved_user.password, user_data['password'])
        self.assertEqual(retrieved_user.email, user_data['email'])
        self.assertEqual(retrieved_user.full_name, user_data['full_name'])
        self.assertEqual(retrieved_user.phone_number, user_data['phone_number'])
        self.assertEqual(retrieved_user.user_type, user_data['user_type'])
        # Add assertions for other attributes as needed

if __name__ == "__main__":
    unittest.main()
