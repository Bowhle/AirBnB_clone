#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """ Test cases for the Place class """

    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_has_attributes(self):
        """Test that Place has the expected attributes"""
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.city_id, "")  # Default value
        self.assertEqual(place.user_id, "")  # Default value
        self.assertEqual(place.name, "")  # Default value
        self.assertEqual(place.description, "")  # Default value
        self.assertEqual(place.number_rooms, 0)  # Default value
        self.assertEqual(place.number_bathrooms, 0)  # Default value
        self.assertEqual(place.max_guest, 0)  # Default value
        self.assertEqual(place.price_by_night, 0)  # Default value
        self.assertEqual(place.latitude, 0.0)  # Default value
        self.assertEqual(place.longitude, 0.0)  # Default value
        self.assertEqual(place.amenity_ids, [])  # Default value

if __name__ == '__main__':
    unittest.main()
