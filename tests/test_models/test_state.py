#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """ Test cases for the State class """

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_has_attributes(self):
        """Test that State has the expected attributes"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")  # Default value

if __name__ == '__main__':
    unittest.main()
