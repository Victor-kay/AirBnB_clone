#!/usr/bin/python3

"""Test class for the Amenity model"""
import unittest
import uuid
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage


class TestAmenity(unittest.TestCase):
    """Test class for the Amenity model"""

    def setUp(self):
        """Setup common tasks for each tests"""
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()

        self.amenity1.name = "Sauna"
        self.amenity2.name = "Swimming Pool"

    def tearDown(self):
        """Clean up necessary clutter after each test"""
        del self.amenity1
        del self.amenity2

    def test_amenity_object_instance(self):
        """Test the object properties of `Amenity` instances"""
        self.assertIsInstance(self.amenity1, Amenity)
        self.assertIsInstance(self.amenity2, Amenity)
        self.assertFalse(self.amenity1 is self.amenity2)
        self.assertTrue(hasattr(self.amenity1, 'name'))
        self.assertTrue(hasattr(self.amenity2, 'name'))

    def test_amenity_inheritance_from_base_model(self):
        """Test for inheritance in `Amenity` from `Base` model"""
        self.assertIsInstance(self.amenity1, BaseModel)
        self.assertIsInstance(self.amenity2, BaseModel)
        self.assertTrue(hasattr(self.amenity1, 'id'))
        self.assertTrue(hasattr(self.amenity2, 'id'))
        self.assertTrue(hasattr(self.amenity1, 'created_at'))
        self.assertTrue(hasattr(self.amenity2, 'created_at'))
        self.assertTrue(hasattr(self.amenity1, 'updated_at'))
        self.assertTrue(hasattr(self.amenity2, 'updated_at'))
        self.assertTrue(hasattr(self.amenity1, 'save'))
        self.assertTrue(hasattr(self.amenity2, 'save'))
        self.assertTrue(hasattr(self.amenity1, 'to_dict'))
        self.assertTrue(hasattr(self.amenity2, 'to_dict'))
        self.assertTrue(hasattr(self.amenity1, '__str__'))
        self.assertTrue(hasattr(self.amenity2, '__str__'))

    def test_amenity_name(self):
        """Test the name property of `Amenity`"""
        self.assertEqual(self.amenity1.name, "Sauna")
        self.assertEqual(self.amenity2.name, "Swimming Pool")

        self.amenity1.name = "Tanzania"
        self.amenity2.name = "Ethiopia"

        self.assertEqual(self.amenity1.name, "Tanzania")
        self.assertEqual(self.amenity2.name, "Ethiopia")

    def test_amenity_str(self):
        """Test the string representation of a `Amenity` object"""
        self.assertEqual(
            self.amenity1.__str__(),
            "[{}] ({}) {}".format(
                self.amenity1.__class__.__name__,
                self.amenity1.id,
                self.amenity1.__dict__
            )
        )
        self.assertEqual(
            self.amenity2.__str__(),
            "[{}] ({}) {}".format(
                self.amenity2.__class__.__name__,
                self.amenity2.id,
                self.amenity2.__dict__
            )
        )

    def test_amenity_to_dict(self):
        """Test the dictionary rep of a `Amenity` object"""

        amenity1_dict = self.amenity1.to_dict()

        self.assertIsInstance(amenity1_dict, dict)
        self.assertTrue('id' in amenity1_dict)
        self.assertTrue('created_at' in amenity1_dict)
        self.assertTrue('updated_at' in amenity1_dict)
        self.assertTrue('__class__' in amenity1_dict)
        self.assertTrue('name' in amenity1_dict)

        self.assertIsInstance(amenity1_dict['id'], str)
        self.assertIsInstance(amenity1_dict['created_at'], str)
        self.assertIsInstance(amenity1_dict['updated_at'], str)
        self.assertIsInstance(amenity1_dict['name'], str)

        self.assertEqual(amenity1_dict['id'], self.amenity1.id)
        self.assertEqual(amenity1_dict['name'], self.amenity1.name)
        self.assertEqual(amenity1_dict['__class__'], "Amenity")

    def test_amenity_args(self):
        """Test that *args is not used"""
        sample_args = [uuid.uuid4(), "Somalia"]
        my_amenity = Amenity(*sample_args)
        self.assertNotEqual(sample_args[0], my_amenity.id)
        self.assertNotEqual(sample_args[1], my_amenity.name)
        self.assertNotEqual(sample_args[1], my_amenity.id)
        self.assertNotEqual(sample_args[0], my_amenity.name)

    def test_amenity_kwargs(self):
        """Test that **kwargs is used to instanciate objects"""
        sample_kwargs = {
            'id': str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(sep="T",
                                                   timespec="microseconds"),
            'updated_at': datetime.now().isoformat(sep="T",
                                                   timespec="microseconds"),
            '__class__': 'DummyAmenity',
            'name': "Jacuzzi"
        }
        my_amenity2 = Amenity(**sample_kwargs)
        self.assertEqual(sample_kwargs['id'], my_amenity2.id)
        self.assertEqual(
            sample_kwargs['created_at'],
            my_amenity2.created_at.isoformat(sep="T", timespec="microseconds"))
        self.assertIsInstance(my_amenity2.created_at, datetime)
        self.assertIsInstance(my_amenity2.updated_at, datetime)
        self.assertEqual(sample_kwargs['name'], my_amenity2.name)
        self.assertNotEqual(sample_kwargs['__class__'], my_amenity2.__class__)

    def test_amenity_save(self):
        """Test that a `Amenity` object is saved to file storage"""
        my_amenity = Amenity()
        my_amenity.save()
        self.assertNotEqual(my_amenity.created_at, my_amenity.updated_at)
