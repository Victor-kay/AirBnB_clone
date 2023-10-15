#!/usr/bin/python3

"""Test class for the City model"""
import unittest
import uuid
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test class for the City model"""

    def setUp(self):
        """Setup common tasks for each tests"""
        self.city1 = City()
        self.city2 = City()

        self.city1.name = "Nairobi"
        self.city2.name = "Kisumu"
        self.city1.state_id = "City." + str(uuid.uuid4())
        self.city2.state_id = "City." + str(uuid.uuid4())

    def tearDown(self):
        """Clean up necessary clutter after each test"""
        del self.city1
        del self.city2

    def test_city_object_instance(self):
        """Test the object properties of City instances"""
        self.assertIsInstance(self.city1, City)
        self.assertIsInstance(self.city2, City)
        self.assertFalse(self.city1 is self.city2)
        self.assertTrue(hasattr(self.city1, 'name'))
        self.assertTrue(hasattr(self.city2, 'name'))
        self.assertTrue(hasattr(self.city1, 'state_id'))
        self.assertTrue(hasattr(self.city2, 'state_id'))

    def test_city_inheritance_from_base_model(self):
        """Test for properties the CIty model inherits from `Base` model"""
        self.assertIsInstance(self.city1, BaseModel)
        self.assertIsInstance(self.city2, BaseModel)
        self.assertTrue(hasattr(self.city1, 'id'))
        self.assertTrue(hasattr(self.city2, 'id'))
        self.assertTrue(hasattr(self.city1, 'created_at'))
        self.assertTrue(hasattr(self.city2, 'created_at'))
        self.assertTrue(hasattr(self.city1, 'updated_at'))
        self.assertTrue(hasattr(self.city2, 'updated_at'))
        self.assertTrue(hasattr(self.city1, 'save'))
        self.assertTrue(hasattr(self.city2, 'save'))
        self.assertTrue(hasattr(self.city1, 'to_dict'))
        self.assertTrue(hasattr(self.city2, 'to_dict'))
        self.assertTrue(hasattr(self.city1, '__str__'))
        self.assertTrue(hasattr(self.city2, '__str__'))

    def test_city_id_unique(self):
        """Test that IDs are unique"""
        self.assertIsInstance(uuid.UUID(self.city1.id), uuid.UUID)
        self.assertIsInstance(uuid.UUID(self.city2.id), uuid.UUID)
        self.assertNotEqual(self.city1.id, self.city2.id)

    def test_city_name(self):
        """Test the name property of `City`"""
        self.assertEqual(self.city1.name, "Nairobi")
        self.assertEqual(self.city2.name, "Kisumu")

        self.city1.name = "Kisii"
        self.city2.name = "Kilifi"

        self.assertEqual(self.city1.name, "Kisii")
        self.assertEqual(self.city2.name, "Kilifi")

    def test_city_state_id(self):
        """Test the `state_id` attribute"""
        self.assertIsInstance(self.city1.state_id, str)
        self.assertIsInstance(uuid.UUID(
            self.city1.state_id.replace("City.", "")), uuid.UUID)

    def test_city_str(self):
        """Test the string representation of a `City` object"""
        self.assertEqual(
            self.city1.__str__(),
            "[{}] ({}) {}".format(
                self.city1.__class__.__name__,
                self.city1.id,
                self.city1.__dict__
            )
        )
        self.assertEqual(
            self.city2.__str__(),
            "[{}] ({}) {}".format(
                self.city2.__class__.__name__,
                self.city2.id,
                self.city2.__dict__
            )
        )

    def test_city_to_dict(self):
        """Test the dictionary rep of a `City` object"""

        city1_dict = self.city1.to_dict()

        self.assertIsInstance(city1_dict, dict)
        self.assertTrue('id' in city1_dict)
        self.assertTrue('created_at' in city1_dict)
        self.assertTrue('updated_at' in city1_dict)
        self.assertTrue('__class__' in city1_dict)
        self.assertTrue('name' in city1_dict)
        self.assertTrue('state_id' in city1_dict)

        self.assertIsInstance(city1_dict['id'], str)
        self.assertIsInstance(city1_dict['created_at'], str)
        self.assertIsInstance(city1_dict['updated_at'], str)
        self.assertIsInstance(city1_dict['name'], str)
        self.assertIsInstance(city1_dict['state_id'], str)

        self.assertEqual(city1_dict['id'], self.city1.id)
        self.assertEqual(city1_dict['name'], self.city1.name)
        self.assertEqual(city1_dict['state_id'], self.city1.state_id)
        self.assertEqual(city1_dict['__class__'], "City")

    def test_city_args(self):
        """Test that *args is not used"""
        sample_args = [uuid.uuid4(), "Lamu", uuid.uuid4()]
        my_city = City(*sample_args)
        self.assertFalse(my_city.id in sample_args)
        self.assertNotEqual(sample_args[1], my_city.name)
        self.assertNotEqual(sample_args[2], my_city.state_id)

    def test_city_kwargs(self):
        """Test that **kwargs is used to instanciate objects"""
        sample_kwargs = {
            'id': str(uuid.uuid4()),
            'state_id': "City." + str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(sep="T",
                                                   timespec="microseconds"),
            'name': 'Naivasha',
            '__class__': 'DummyState',
        }
        my_city = City(**sample_kwargs)
        self.assertEqual(sample_kwargs['id'], my_city.id)
        self.assertEqual(
            sample_kwargs['created_at'],
            my_city.created_at.isoformat(sep="T", timespec="microseconds"))
        self.assertEqual(sample_kwargs['name'], my_city.name)
        self.assertEqual(sample_kwargs['state_id'], my_city.state_id)
        self.assertNotEqual(sample_kwargs['__class__'], my_city.__class__)

    def test_city_save(self):
        """Test that a `City` object is saved to file storage"""
        pass
