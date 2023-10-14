#!/usr/bin/python3

"""Module containing tests for the File Storage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
# from models import storage


class TestFileStorage(unittest.TestCase):
    """Test class for the file storage model"""

    def test_file_path(self):
        """Tests that the file path exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertEqual(FileStorage._FileStorage__file_path, 'data.json')

    def test_reload(self):
        """Test that objects are loaded into the program"""
        pass

    def test_save(self):
        """Test that objects are saved to a file in JSON"""
        self.base_obj1 = BaseModel()
        self.base_obj1.name = "Peter"
        self.base_obj1.age = 20
        self.base_obj1.save()
