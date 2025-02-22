#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """ Test cases for the City class """

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_has_attributes(self):
        """Test that City has the expected attributes"""
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")  # Default value
        self.assertEqual(city.name, "")  # Default value

if __name__ == '__main__':
    unittest.main()
