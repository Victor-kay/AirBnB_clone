#!/usr/bin/python3

"""User test module

    Contains unit tests of the user model
"""

import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unit tests for the user model"""

    def setUp(self):
        """Set up configurations before each test"""
        self.my_user1 = User()
        self.my_user2 = User()

        self.my_user1.first_name = "John"
        self.my_user1.last_name = "Doe"
        self.my_user1.email = "johndoe@mail.com"
        self.my_user1.password = "^johndoe@doejohn$"

        self.my_user2.first_name = "Jane"
        self.my_user2.last_name = "Mkenya"
        self.my_user2.email = "janemkenya@mail.com"
        self.my_user2.password = "^janemkenya@mkenyajane$"

    def tearDown(self):
        """Tear down after each test runs"""
        pass

    def test_user_object(self):
        """Test the existence and properties of the user object"""
        self.assertIsInstance(self.my_user1, User)
        self.assertTrue(hasattr(self.my_user1, 'first_name'),
                        "First name attribute does not exist")
        self.assertTrue(hasattr(self.my_user1, 'last_name'),
                        "Last name attribute does not exist")
        self.assertTrue(hasattr(self.my_user1, 'email'),
                        "Email attribute does not exist")
        self.assertTrue(hasattr(self.my_user1, 'password'),
                        "Password attribute does not exist")

    def test_user_base_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(self.my_user1, BaseModel)
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(hasattr(self.my_user1, 'id'))
        self.assertTrue(hasattr(self.my_user1, 'created_at'))
        self.assertTrue(hasattr(self.my_user1, 'updated_at'))
        self.assertTrue(hasattr(self.my_user1, 'to_dict'))
        self.assertTrue(hasattr(self.my_user1, 'save'))

    def test_user_first_name(self):
        """Test cases for a user's `first_name`"""
        self.assertEqual(self.my_user1.first_name, "John")
        self.assertEqual(self.my_user2.first_name, "Jane")

        self.my_user1.first_name = "James"
        self.my_user2.first_name = "Tracy"

        self.assertEqual(self.my_user1.first_name, 'James')
        self.assertEqual(self.my_user2.first_name, 'Tracy')

    def test_user_last_name(self):
        """Test cases for a user's `last_name`"""
        self.assertEqual(self.my_user1.last_name, "Doe")
        self.assertEqual(self.my_user2.last_name, "Mkenya")

        self.my_user1.last_name = "dirisha"
        self.my_user2.last_name = "mlango"

        self.assertEqual(self.my_user1.last_name, 'dirisha')
        self.assertEqual(self.my_user2.last_name, 'mlango')

    def test_user_email(self):
        """Test cases for a user's `email`"""
        self.assertEqual(self.my_user1.email, "johndoe@mail.com")
        self.assertEqual(self.my_user2.email, "janemkenya@mail.com")

        self.my_user1.email = "johndirisha@mail.com"
        self.my_user2.email = "janemlango@mail.com"

        self.assertEqual(self.my_user1.email, 'johndirisha@mail.com')
        self.assertEqual(self.my_user2.email, 'janemlango@mail.com')

    def test_user_password(self):
        """Test cases for a user's `password`"""
        self.assertEqual(self.my_user1.password, "^johndoe@doejohn$")
        self.assertEqual(self.my_user2.password, "^janemkenya@mkenyajane$")

        self.my_user1.password = "^johndirisha@dirishajohn$"
        self.my_user2.password = "^janemlango@mlangojane$"

        self.assertEqual(self.my_user1.password, '^johndirisha@dirishajohn$')
        self.assertEqual(self.my_user2.password, '^janemlango@mlangojane$')

    def test_user_str(self):
        """Test cases for printing a string rep of a user object"""
        self.assertEqual(
            self.my_user1.__str__(),
            "[{}] ({}) {}".format(
                self.my_user1.__class__.__name__,
                self.my_user1.id,
                self.my_user1.__dict__
                ))

    def test_user_to_dict(self):
        """Test the required dictionary rep of an object instance"""
        my_user_dict = self.my_user1.to_dict()
        # assert instance is `dictionary`
        self.assertIsInstance(my_user_dict, dict)

        # assert properties and their types
        self.assertTrue('id' in my_user_dict)
        self.assertTrue('created_at' in my_user_dict)
        self.assertTrue('updated_at' in my_user_dict)
        self.assertTrue('first_name' in my_user_dict)
        self.assertTrue('last_name' in my_user_dict)
        self.assertTrue('email' in my_user_dict)
        self.assertTrue('password' in my_user_dict)
        self.assertTrue(type(my_user_dict['id']) is str)
        self.assertTrue(type(my_user_dict['created_at']) is str)
        self.assertTrue(type(my_user_dict['updated_at']) is str)
        self.assertTrue(type(my_user_dict['first_name']) is str)
        self.assertTrue(type(my_user_dict['last_name']) is str)
        self.assertTrue(type(my_user_dict['email']) is str)
        self.assertTrue(type(my_user_dict['password']) is str)
        self.assertTrue(type(my_user_dict['__class__']) is str)

        # assert values of resulting dict
        self.assertEqual(my_user_dict['id'], self.my_user1.id)
        self.assertEqual(my_user_dict['first_name'], self.my_user1.first_name)
        self.assertEqual(my_user_dict['last_name'], self.my_user1.last_name)
        self.assertEqual(my_user_dict['email'], self.my_user1.email)
        self.assertEqual(my_user_dict['password'], self.my_user1.password)
        self.assertEqual(my_user_dict['__class__'], "User")
