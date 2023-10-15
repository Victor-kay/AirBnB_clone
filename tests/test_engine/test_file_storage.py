#!/usr/bin/python3

"""Module containing tests for the File Storage class"""

import unittest
import os
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test class for the file storage model"""

    @classmethod
    def setUpClass(self):
        """Set up a one time procedure for the entire test run"""
        self.my_model = BaseModel()

    def setUp(self):
        """Set up a common procedure for each test"""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = 'file.json'

    def test_storage_instance(self):
        """Tests the existence of the storage instance"""
        self.assertIsInstance(storage, FileStorage)

    def test_storage_attributes(self):
        """Tests the attributes of the storage instance"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertIn('new', FileStorage.__dict__)
        self.assertIn('save', FileStorage.__dict__)
        self.assertIn('reload', FileStorage.__dict__)
        self.assertIn('all', FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage.new, object)
        self.assertIsInstance(FileStorage.save, object)
        self.assertIsInstance(FileStorage.reload, object)
        self.assertIsInstance(FileStorage.all, object)

    def test_objects(self):
        """Tests the existence of the objects dictionary"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_file_path(self):
        """Tests that the file path exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertEqual(FileStorage._FileStorage__file_path, 'file.json')

    def test_storage_all(self):
        """Test that the all method returns the __objects attribute"""
        self.assertEqual(storage.all(), FileStorage._FileStorage__objects)

    def test_storage_new(self):
        """Test that new adds an object to the __objects attribute"""
        my_user = User()
        my_user.first_name = "Hellen"
        my_user.last_name = "Linux"
        self.assertIn(my_user, FileStorage._FileStorage__objects.values())
        self.assertEqual(len(FileStorage._FileStorage__objects), 1)
        self.assertEqual(len(storage.all()), 1)
        self.assertEqual(my_user.first_name, FileStorage._FileStorage__objects[
                            'User.' + my_user.id].first_name)
        self.assertEqual(my_user.last_name, FileStorage._FileStorage__objects[
                            'User.' + my_user.id].last_name)

    def test_storage_save(self):
        """Test that save writes the __objects attribute to a file"""
        my_model_2 = BaseModel()
        my_model_2.name = "Boxer"
        my_model_2.save()
        self.assertIn(my_model_2, FileStorage._FileStorage__objects.values())
        self.assertEqual(len(FileStorage._FileStorage__objects), 1)
