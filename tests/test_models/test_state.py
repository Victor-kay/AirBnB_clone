#!/usr/bin/python3

"""Test class for the State model"""
import unittest
import uuid
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage


class TestState(unittest.TestCase):
    """Test class for the State model"""

    def setUp(self):
        """Setup common tasks for each tests"""
        self.state1 = State()
        self.state2 = State()

        self.state1.name = "Kenya"
        self.state2.name = "Uganda"

    def tearDown(self):
        """Clean up necessary clutter after each test"""
        del self.state1
        del self.state2

    def test_state_object_instance(self):
        """Test the object properties of state instances"""
        self.assertIsInstance(self.state1, State)
        self.assertIsInstance(self.state2, State)
        self.assertFalse(self.state1 is self.state2)
        self.assertTrue(hasattr(self.state1, 'name'))
        self.assertTrue(hasattr(self.state2, 'name'))

    def test_state_inheritance_from_base_model(self):
        """Test for properties the state model inherits from `Base` model"""
        self.assertIsInstance(self.state1, BaseModel)
        self.assertIsInstance(self.state2, BaseModel)
        self.assertTrue(hasattr(self.state1, 'id'))
        self.assertTrue(hasattr(self.state2, 'id'))
        self.assertTrue(hasattr(self.state1, 'created_at'))
        self.assertTrue(hasattr(self.state2, 'created_at'))
        self.assertTrue(hasattr(self.state1, 'updated_at'))
        self.assertTrue(hasattr(self.state2, 'updated_at'))
        self.assertTrue(hasattr(self.state1, 'save'))
        self.assertTrue(hasattr(self.state2, 'save'))
        self.assertTrue(hasattr(self.state1, 'to_dict'))
        self.assertTrue(hasattr(self.state2, 'to_dict'))
        self.assertTrue(hasattr(self.state1, '__str__'))
        self.assertTrue(hasattr(self.state2, '__str__'))

    def test_state_name(self):
        """Test the name property of `state`"""
        self.assertEqual(self.state1.name, "Kenya")
        self.assertEqual(self.state2.name, "Uganda")

        self.state1.name = "Tanzania"
        self.state2.name = "Ethiopia"

        self.assertEqual(self.state1.name, "Tanzania")
        self.assertEqual(self.state2.name, "Ethiopia")

    def test_state_str(self):
        """Test the string representation of a `state` object"""
        self.assertEqual(
            self.state1.__str__(),
            "[{}] ({}) {}".format(
                self.state1.__class__.__name__,
                self.state1.id,
                self.state1.__dict__
            )
        )
        self.assertEqual(
            self.state2.__str__(),
            "[{}] ({}) {}".format(
                self.state2.__class__.__name__,
                self.state2.id,
                self.state2.__dict__
            )
        )

    def test_state_to_dict(self):
        """Test the dictionary rep of a `State` object"""

        state1_dict = self.state1.to_dict()

        self.assertIsInstance(state1_dict, dict)
        self.assertTrue('id' in state1_dict)
        self.assertTrue('created_at' in state1_dict)
        self.assertTrue('updated_at' in state1_dict)
        self.assertTrue('__class__' in state1_dict)
        self.assertTrue('name' in state1_dict)

        self.assertIsInstance(state1_dict['id'], str)
        self.assertIsInstance(state1_dict['created_at'], str)
        self.assertIsInstance(state1_dict['updated_at'], str)
        self.assertIsInstance(state1_dict['name'], str)

        self.assertEqual(state1_dict['id'], self.state1.id)
        self.assertEqual(state1_dict['name'], self.state1.name)
        self.assertEqual(state1_dict['__class__'], "State")

    def test_state_args(self):
        """Test that *args is not used"""
        sample_args = [uuid.uuid4(), "Somalia"]
        my_state = State(*sample_args)
        self.assertNotEqual(sample_args[0], my_state.id)
        self.assertNotEqual(sample_args[1], my_state.name)
        self.assertNotEqual(sample_args[1], my_state.id)
        self.assertNotEqual(sample_args[0], my_state.name)

    def test_state_kwargs(self):
        """Test that **kwargs is used to instanciate objects"""
        sample_kwargs = {
            'id': str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(sep="T",
                                                   timespec="microseconds"),
            '__class__': 'DummyState',
            'name': "Sudan"
        }
        my_state2 = State(**sample_kwargs)
        self.assertEqual(sample_kwargs['id'], my_state2.id)
        self.assertEqual(
            sample_kwargs['created_at'],
            my_state2.created_at.isoformat(sep="T", timespec="microseconds"))
        self.assertEqual(sample_kwargs['name'], my_state2.name)
        self.assertNotEqual(sample_kwargs['__class__'], my_state2.__class__)

    def test_state_save(self):
        """Test that a `State` object is saved to file storage"""
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)
