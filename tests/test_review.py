#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """ Test cases for the Review class """

    def test_is_subclass(self):
        """Test that Review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_has_attributes(self):
        """Test that Review has the expected attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")  # Default value
        self.assertEqual(review.user_id, "")  # Default value
        self.assertEqual(review.text, "")  # Default value

if __name__ == '__main__':
    unittest.main()
