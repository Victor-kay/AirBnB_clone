#!/usr/bin/python3

"""Module containing tests for the Base Model class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for the Base Model"""

    def test_uuid(self):
        """Test the id property of the Base Model"""
        self.base_object1 = BaseModel()
        self.base_object2 = BaseModel()
        self.assertIsInstance(self.base_object1, BaseModel)
        self.assertTrue(hasattr(self.base_object1, "id"))
        self.assertIsInstance(self.base_object1.id, str)
        self.assertNotEqual(self.base_object1, self.base_object2)

    def test_created_at(self):
        """Test the `created_at` property"""
        self.base_created_at = BaseModel()
        self.assertIsInstance(self.base_created_at, BaseModel)
        self.assertTrue(hasattr(self.base_created_at, 'created_at'))
        self.assertIsInstance(self.base_created_at.created_at, datetime)

    def test_updated_at(self):
        """Test the `updated_at` property"""
        self.base_updated_at = BaseModel()
        self.assertIsInstance(self.base_updated_at, BaseModel)
        self.assertTrue(hasattr(self.base_updated_at, 'updated_at'))
        self.assertIsInstance(self.base_updated_at.updated_at, datetime)

    def test_str(self):
        """Test the `__str__` method"""
        self.base_str = BaseModel()
        self.assertIsInstance(self.base_str, BaseModel)
        self.assertTrue(hasattr(BaseModel.__dict__, '__str__'))
        self.assertEqual(self.base_str.__str__(),
                         "[{}] ({}) {}".format(
                             self.base_str.__class__.__name__,
                             self.base_str.id,
                             self.base_str.__dict__
                         ))

    def test_to_dict(self):
        """Test the `to_dict` method that returns the dictionary
        representation of an object"""
        self.assertTrue(hasattr(BaseModel, 'to_dict'))
        self.assertTrue('to_dict' in dir(BaseModel))
        self.result_dict = BaseModel().to_dict()
        self.assertIsInstance(self.result_dict, dict)
        self.assertTrue('id' in self.result_dict)
        self.assertTrue('created_at' in self.result_dict)
        self.assertTrue('updated_at' in self.result_dict)
        self.assertTrue('__class__' in self.result_dict)
        self.assertEqual(self.result_dict['__class__'], 'BaseModel')
        self.assertIsInstance(self.result_dict['created_at'], str)
        self.assertIsInstance(self.result_dict['updated_at'], str)
