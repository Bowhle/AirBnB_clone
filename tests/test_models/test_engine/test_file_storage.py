#!/usr/bin/python3
import unittest
import os
import json
from models.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Setup before each test."""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.user = User()
        # Clear objects for a clean test environment
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test that all() returns the correct dictionary of objects."""
        self.storage.new(self.obj)
        self.storage.new(self.user)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn(f"BaseModel.{self.obj.id}", all_objects)
        self.assertIn(f"User.{self.user.id}", all_objects)

    def test_new(self):
        """Test that new() correctly adds an object to the storage."""
        self.storage.new(self.obj)
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.obj.id}", all_objects)

    def test_save(self):
        """Test that save() correctly serializes objects to the file."""
        self.storage.new(self.obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            data = json.load(file)
            self.assertIn(f"BaseModel.{self.obj.id}", data)

    def test_reload(self):
        """Test that reload() correctly loads objects from the file."""
        self.storage.new(self.obj)
        self.storage.save()
        # Clear objects to ensure reload works
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.obj.id}", all_objects)

    def test_reload_file_not_found(self):
        """Test that reload() does nothing if the file does not exist."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        # Ensure objects are empty after reload
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)


if __name__ == "__main__":
    unittest.main()
