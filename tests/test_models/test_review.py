#!/usr/bin/python3

"""Test class for the Review model"""
import unittest
import uuid
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage


class TestReview(unittest.TestCase):
    """Test class for the Review model"""

    def setUp(self):
        """Setup common tasks for each tests"""
        self.review1 = Review()
        self.review2 = Review()

        self.review1.place_id = "Place." + str(uuid.uuid4())
        self.review1.user_id = "User." + str(uuid.uuid4())
        self.review1.text = "Half the staff were passively rude"
        self.review2.place_id = "Place." + str(uuid.uuid4())
        self.review2.user_id = "User." + str(uuid.uuid4())
        self.review2.text = "The scenery is serene and the food is yummy"

    def tearDown(self):
        """Clean up necessary clutter after each test"""
        del self.review1
        del self.review2

    def test_review_object_instance(self):
        """Test the object properties of Review instances"""
        self.assertIsInstance(self.review1, Review)
        self.assertIsInstance(self.review2, Review)
        self.assertFalse(self.review1 is self.review2)
        self.assertFalse(self.review1 == self.review2)
        self.assertTrue(hasattr(self.review1, 'text'))
        self.assertTrue(hasattr(self.review2, 'text'))
        self.assertTrue(hasattr(self.review1, 'place_id'))
        self.assertTrue(hasattr(self.review2, 'place_id'))
        self.assertTrue(hasattr(self.review1, 'user_id'))
        self.assertTrue(hasattr(self.review2, 'user_id'))

    def test_review_inheritance_from_base_model(self):
        """Test for properties the CIty model inherits from `Base` model"""
        self.assertIsInstance(self.review1, BaseModel)
        self.assertIsInstance(self.review2, BaseModel)
        self.assertTrue(hasattr(self.review1, 'id'))
        self.assertTrue(hasattr(self.review2, 'id'))
        self.assertTrue(hasattr(self.review1, 'created_at'))
        self.assertTrue(hasattr(self.review2, 'created_at'))
        self.assertTrue(hasattr(self.review1, 'updated_at'))
        self.assertTrue(hasattr(self.review2, 'updated_at'))
        self.assertTrue(hasattr(self.review1, 'save'))
        self.assertTrue(hasattr(self.review2, 'save'))
        self.assertTrue(hasattr(self.review1, 'to_dict'))
        self.assertTrue(hasattr(self.review2, 'to_dict'))
        self.assertTrue(hasattr(self.review1, '__str__'))
        self.assertTrue(hasattr(self.review2, '__str__'))

    def test_review_id_unique(self):
        """Test review `id`"""
        self.assertIsInstance(uuid.UUID(self.review1.id), uuid.UUID)
        self.assertIsInstance(uuid.UUID(self.review2.id), uuid.UUID)
        self.assertNotEqual(self.review1.id, self.review2.id)

    def test_review_attr_types(self):
        """Test attribute typed for a review object"""
        self.assertIsInstance(self.review1.id, str)
        self.assertIsInstance(self.review1.created_at, datetime)
        self.assertIsInstance(self.review1.updated_at, datetime)
        self.assertIsInstance(self.review1.place_id, str)
        self.assertIsInstance(self.review1.user_id, str)
        self.assertIsInstance(self.review1.text, str)

    def test_review_text(self):
        """Test the text property of `Review`"""
        self.assertEqual(self.review1.text,
                         "Half the staff were passively rude")
        self.assertEqual(self.review2.text,
                         "The scenery is serene and the food is yummy")

        self.review1.text = "Absolute madness"
        self.review2.text = "My room was cold.they denied a room change.1 star"

        self.assertEqual(self.review1.text, "Absolute madness")
        self.assertEqual(self.review2.text,
                         "My room was cold.they denied a room change.1 star")

    def test_review_place_id(self):
        """Test the `place_id` attribute"""
        self.assertIsInstance(uuid.UUID(
            self.review1.place_id.replace("Place.", "")), uuid.UUID)

    def test_review_user_id(self):
        """Test the `user_id` attribute"""
        self.assertIsInstance(uuid.UUID(
            self.review1.user_id.replace("User.", "")), uuid.UUID)

    def test_review_str(self):
        """Test the string representation of a `Review` object"""
        self.assertEqual(
            self.review1.__str__(),
            "[{}] ({}) {}".format(
                self.review1.__class__.__name__,
                self.review1.id,
                self.review1.__dict__
            )
        )
        self.assertEqual(
            self.review2.__str__(),
            "[{}] ({}) {}".format(
                self.review2.__class__.__name__,
                self.review2.id,
                self.review2.__dict__
            )
        )

    def test_review_to_dict(self):
        """Test the dictionary rep of a `Review` object"""

        review1_dict = self.review1.to_dict()

        self.assertIsInstance(review1_dict, dict)
        self.assertTrue('id' in review1_dict)
        self.assertTrue('created_at' in review1_dict)
        self.assertTrue('updated_at' in review1_dict)
        self.assertTrue('__class__' in review1_dict)
        self.assertTrue('text' in review1_dict)
        self.assertTrue('place_id' in review1_dict)

        self.assertIsInstance(review1_dict['id'], str)
        self.assertIsInstance(review1_dict['created_at'], str)
        self.assertIsInstance(review1_dict['updated_at'], str)
        self.assertIsInstance(review1_dict['text'], str)
        self.assertIsInstance(review1_dict['place_id'], str)

        self.assertEqual(review1_dict['id'], self.review1.id)
        self.assertEqual(review1_dict['text'], self.review1.text)
        self.assertEqual(review1_dict['place_id'], self.review1.place_id)
        self.assertEqual(review1_dict['__class__'], "Review")

    def test_review_args(self):
        """Test that *args is not used"""
        sample_args = [uuid.uuid4(),
                       "Staff was kind. ENjoyed my stay", uuid.uuid4()]
        my_review = Review(*sample_args)
        self.assertFalse(my_review.id in sample_args)
        self.assertNotEqual(sample_args[1], my_review.text)
        self.assertNotEqual(sample_args[2], my_review.place_id)

    def test_review_kwargs(self):
        """Test that **kwargs is used to instanciate objects"""
        sample_kwargs = {
            'id': str(uuid.uuid4()),
            'place_id': "Place." + str(uuid.uuid4()),
            'user_id': "User." + str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(sep="T",
                                                   timespec="microseconds"),
            'updated_at': datetime.now().isoformat(sep="T",
                                                   timespec="microseconds"),
            'text': 'The place is amazing. The jacuzzi was so relaxing',
            '__class__': 'DummyState',
        }
        my_review = Review(**sample_kwargs)
        self.assertEqual(sample_kwargs['id'], my_review.id)
        self.assertEqual(sample_kwargs['created_at'],
                         my_review.created_at.isoformat(
                             sep="T", timespec="microseconds"))
        self.assertIsInstance(my_review.created_at, datetime)
        self.assertIsInstance(my_review.updated_at, datetime)
        self.assertEqual(sample_kwargs['text'], my_review.text)
        self.assertEqual(sample_kwargs['place_id'], my_review.place_id)
        self.assertEqual(sample_kwargs['user_id'], my_review.user_id)
        self.assertNotEqual(sample_kwargs['__class__'], my_review.__class__)

    def test_review_save(self):
        """Test that a `Review` object is saved to file storage"""
        self.review1.save()
        self.review2.save()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)
        self.assertNotEqual(self.review2.created_at, self.review2.updated_at)
