#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test the User class."""

    def test_instance(self):
        """Test that User is an instance of both User and BaseModel."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        """Test the default values of the User class attributes."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        """Test the to_dict method of User."""
        user = User()
        user_dict = user.to_dict()
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "")
        self.assertEqual(user_dict["password"], "")
        self.assertEqual(user_dict["first_name"], "")
        self.assertEqual(user_dict["last_name"], "")

    def test_save(self):
        """Test the save method of User (if it is defined in BaseModel)."""
        user = User()
        old_updated_at = user.updated_at
        user.save()  # Assuming save updates the `updated_at` attribute
        self.assertNotEqual(user.updated_at, old_updated_at)

if __name__ == "__main__":
    unittest.main()
