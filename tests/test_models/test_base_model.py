#!/usr/bin/python3
"""
    A class that tests the BaseModel to ensure it is working properly
    using unit tests.
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep


class TestBaseModelInstantiation(unittest.TestCase):
    """ Tests for the BaseModel class instantiation. """
    def test_no_args_instance(self):
        """ Test if the model works with no args passed. """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_if_id_is_string(self):
        """ Test if the id is of type string. """
        Bm1 = BaseModel()
        self.assertEqual(str, type(Bm1.id))

    def test_if_id_is_not_others(self):
        """ Test if id is not any other type than string. """
        Bm1 = BaseModel()
        self.assertNotEqual(int, type(Bm1.id))
        self.assertNotEqual(float, type(Bm1.id))
        self.assertNotEqual(list, type(Bm1.id))
        self.assertNotEqual(dict, type(Bm1.id))
        self.assertNotEqual(set, type(Bm1.id))

    def test_two_models_id(self):
        """ Test that two different objects have different ids. """
        Bm1 = BaseModel()
        Bm2 = BaseModel()
        self.assertNotEqual(Bm1.id, Bm2.id)

    def test_created_at(self):
        """ Test if created_at is a datetime object. """
        Bm1 = BaseModel()
        self.assertEqual(datetime, type(Bm1.created_at))

    def test_updated_at(self):
        """ Test if updated_at is a datetime object. """
        Bm1 = BaseModel()
        self.assertEqual(datetime, type(Bm1.updated_at))

    def test_created_at_is_less_than_update_at(self):
        """ Test that created_at is less than updated_at after save(). """
        Bm1 = BaseModel()
        time_created = Bm1.created_at
        Bm1.save()
        self.assertLess(time_created, Bm1.updated_at)

    def test_str_rep(self):
        """ Test the string representation of the BaseModel object. """
        dt = datetime.now()
        Bm1 = BaseModel()
        Bm1.id = "23456"
        Bm1.number = 1997
        Bm1.name = "My first Model"
        Bm1.created_at = dt
        Bm1.updated_at = dt
        Bm1str = Bm1.__str__()
        self.assertIn("[BaseModel] (23456)", Bm1str)
        self.assertIn("'id': '23456'", Bm1str)
        self.assertIn("'number': 1997", Bm1str)
        self.assertIn("'name': 'My first Model'", Bm1str)
        self.assertIn("'updated_at': " + repr(dt), Bm1str)
        self.assertIn("'created_at': " + repr(dt), Bm1str)

    def test_args_with_args(self):
        """ Test if the arguments passed to the constructor work. """
        Bm1 = BaseModel(id="123")
        self.assertEqual(Bm1.id, "123")


class TestBaseModelSave(unittest.TestCase):
    """ Tests for the save method of BaseModel. """
    def test_save_once(self):
        """ Test if save updates the updated_at time. """
        Bm1 = BaseModel()
        sleep(1)
        first_update = Bm1.updated_at
        Bm1.save()
        self.assertLess(first_update, Bm1.updated_at)

    def test_save_twice(self):
        """ Test if saving twice updates updated_at again. """
        Bm1 = BaseModel()
        sleep(1)
        first_update = Bm1.updated_at
        Bm1.save()
        second_update = Bm1.updated_at
        Bm1.save()
        self.assertLess(first_update, second_update)


if __name__ == "__main__":
    unittest.main()
