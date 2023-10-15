#!/usr/bin/python3

"""Test class for the Place model"""
import unittest
import uuid
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage


class TestPlace(unittest.TestCase):
    """Test class for the Place model"""

    def setUp(self):
        """Setup common tasks for each tests"""
        self.place1 = Place()
        self.place2 = Place()

        self.place1.city_id = "City." + str(uuid.uuid4())
        self.place1.user_id = "User." + str(uuid.uuid4())
        self.place1.name = "Tango Villas"
        self.place1.description = "Enjoy the scenery over the national park"
        self.place1.number_rooms = 3
        self.place1.number_bathrooms = 4
        self.place1.max_guest = 6
        self.place1.price_by_night = 35000
        self.place1.latitude = 45.034
        self.place1.longitude = 145.034
        self.place1.amenity_ids = ["Amenity." + str(uuid.uuid4()),
                                   "Amenity." + str(uuid.uuid4()),
                                   "Amenity." + str(uuid.uuid4())]
        self.place2.city_id = "City." + str(uuid.uuid4())
        self.place2.user_id = "User." + str(uuid.uuid4())
        self.place2.name = "Spicy Valleys"
        self.place2.description = "Spacious room with all your needs"
        self.place2.number_rooms = 2
        self.place2.number_bathrooms = 3
        self.place2.max_guest = 4
        self.place2.price_by_night = 15000
        self.place2.latitude = 23.034
        self.place2.longitude = -45.034
        self.place2.amenity_ids = ["Amenity." + str(uuid.uuid4()),
                                   "Amenity." + str(uuid.uuid4()),
                                   "Amenity." + str(uuid.uuid4())]

    def tearDown(self):
        """Clean up necessary clutter after each test"""
        del self.place1
        del self.place2

    def test_place_object_instance(self):
        """Test the object properties of Place instances"""
        self.assertIsInstance(self.place1, Place)
        self.assertFalse(self.place1 is self.place2)
        self.assertFalse(self.place1 == self.place2)
        self.assertIn('description', self.place1.__dict__)
        self.assertIn('city_id', self.place1.__dict__)
        self.assertIn('user_id', self.place1.__dict__)
        self.assertIn('name', self.place1.__dict__)
        self.assertIn('description', self.place1.__dict__)
        self.assertIn('number_rooms', self.place1.__dict__)
        self.assertIn('number_bathrooms', self.place1.__dict__)
        self.assertIn('max_guest', self.place1.__dict__)
        self.assertIn('price_by_night', self.place1.__dict__)
        self.assertIn('latitude', self.place1.__dict__)
        self.assertIn('longitude', self.place1.__dict__)
        self.assertIn('amenity_ids', self.place1.__dict__)

    def test_place_attr_types(self):
        """Test the attribute types of the `Place` object"""
        self.assertIsInstance(self.place1.id, str)
        self.assertIsInstance(self.place1.created_at, datetime)
        self.assertIsInstance(self.place1.updated_at, datetime)
        self.assertIsInstance(self.place1.city_id, str)
        self.assertIsInstance(self.place1.user_id, str)
        self.assertIsInstance(self.place1.name, str)
        self.assertIsInstance(self.place1.description, str)
        self.assertIsInstance(self.place1.number_rooms, int)
        self.assertIsInstance(self.place1.number_bathrooms, int)
        self.assertIsInstance(self.place1.max_guest, int)
        self.assertIsInstance(self.place1.price_by_night, int)
        self.assertIsInstance(self.place1.latitude, float)
        self.assertIsInstance(self.place1.longitude, float)
        self.assertIsInstance(self.place1.amenity_ids, list)
        self.assertIsInstance(self.place1.amenity_ids[0], str)

    def test_place_inheritance_from_base_model(self):
        """Test for properties the Place model inherits from `Base` model"""
        self.assertIsInstance(self.place1, BaseModel)
        self.assertIsInstance(self.place2, BaseModel)
        self.assertTrue(hasattr(self.place1, 'id'))
        self.assertTrue(hasattr(self.place2, 'id'))
        self.assertTrue(hasattr(self.place1, 'created_at'))
        self.assertTrue(hasattr(self.place2, 'created_at'))
        self.assertTrue(hasattr(self.place1, 'updated_at'))
        self.assertTrue(hasattr(self.place2, 'updated_at'))
        self.assertTrue(hasattr(self.place1, 'save'))
        self.assertTrue(hasattr(self.place2, 'save'))
        self.assertTrue(hasattr(self.place1, 'to_dict'))
        self.assertTrue(hasattr(self.place2, 'to_dict'))
        self.assertTrue(hasattr(self.place1, '__str__'))
        self.assertTrue(hasattr(self.place2, '__str__'))

    def test_place_description(self):
        """Test the description property of `Place`"""
        self.assertEqual(self.place1.description,
                         "Enjoy the scenery over the national park")
        self.assertEqual(self.place2.description,
                         "Spacious room with all your needs")

        self.place1.description = "All the rooms you want"
        self.place2.description = "Take a dive in the swimming pool"

        self.assertEqual(self.place1.description, "All the rooms you want")
        self.assertEqual(self.place2.description,
                         "Take a dive in the swimming pool")

    def test_place_id_unique(self):
        """Test that `id` are never equal"""
        self.assertNotEqual(self.place1.id, self.place2.id)

    def test_place_city_id(self):
        """Test the `city_id` attribute"""
        self.assertIsInstance(uuid.UUID(
            self.place1.city_id.replace("City.", "")), uuid.UUID)

    def test_place_user_id(self):
        """Test the `user_id` attribute"""
        self.assertIsInstance(uuid.UUID(
            self.place1.user_id.replace("User.", "")), uuid.UUID)

    def test_place_name(self):
        """Test the `name` attribute"""
        self.assertEqual(self.place1.name, "Tango Villas")
        self.place1.name = "Orange Crossroads"
        self.assertEqual(self.place1.name, "Orange Crossroads")

    def test_place_description(self):
        """Test the `description` attribute"""
        self.assertEqual(self.place1.description,
                         "Enjoy the scenery over the national park")
        self.place1.description = "Explore the enchanting parks"
        self.assertEqual(
            self.place1.description, "Explore the enchanting parks")

    def test_place_number_rooms(self):
        """Test the `number_rooms` attribute"""
        self.assertEqual(self.place1.number_rooms, 3)
        self.place1.number_rooms = 4
        self.assertEqual(self.place1.number_rooms, 4)

    def test_place_number_bathrooms(self):
        """Test the `number_bathrooms` attribute"""
        self.assertEqual(self.place1.number_bathrooms, 4)
        self.place1.number_bathrooms = 2
        self.assertEqual(self.place1.number_bathrooms, 2)

    def test_place_max_guest(self):
        """Test the `max_guest` attribute"""
        self.assertEqual(self.place1.max_guest, 6)
        self.place1.max_guest = 5
        self.assertEqual(self.place1.max_guest, 5)

    def test_place_price_by_night(self):
        """Test the `price_by_night` attribute"""
        self.assertEqual(self.place1.price_by_night, 35000)
        self.place1.price_by_night = 30000
        self.assertEqual(self.place1.price_by_night, 30000)

    def test_place_latitude(self):
        """Test the `latitude` attribute"""
        self.assertEqual(self.place1.latitude, 45.034)
        self.place1.latitude = 12.876
        self.assertEqual(self.place1.latitude, 12.876)

    def test_place_longitude(self):
        """Test the `longitude` attribute"""
        self.assertEqual(self.place1.longitude, 145.034)
        self.place1.longitude = 43.67
        self.assertEqual(self.place1.longitude, 43.67)

    def test_place_amenity_ids(self):
        """Test the `amenity_ids` attribute"""
        amenity_ids_sample = [
            "Amenity." + str(uuid.uuid4()),
            "Amenity." + str(uuid.uuid4()),
        ]
        self.place1.amenity_ids = amenity_ids_sample
        self.assertListEqual(self.place1.amenity_ids, amenity_ids_sample)
        self.assertEqual(len(self.place1.amenity_ids), len(amenity_ids_sample))

    def test_place_str(self):
        """Test the string representation of a `Place` object"""
        self.assertEqual(
            self.place1.__str__(),
            "[{}] ({}) {}".format(
                self.place1.__class__.__name__,
                self.place1.id,
                self.place1.__dict__
            )
        )
        self.assertEqual(
            self.place2.__str__(),
            "[{}] ({}) {}".format(
                self.place2.__class__.__name__,
                self.place2.id,
                self.place2.__dict__
            )
        )

    def test_place_to_dict(self):
        """Test the dictionary rep of a `Place` object"""

        place1_dict = self.place1.to_dict()

        self.assertIsInstance(place1_dict, dict)
        self.assertTrue('id' in place1_dict)
        self.assertTrue('created_at' in place1_dict)
        self.assertTrue('updated_at' in place1_dict)
        self.assertTrue('__class__' in place1_dict)
        self.assertTrue('description' in place1_dict)
        self.assertTrue('city_id' in place1_dict)
        self.assertTrue('user_id' in place1_dict)
        self.assertIn('name', place1_dict)
        self.assertIn('number_rooms', place1_dict)
        self.assertIn('number_bathrooms', place1_dict)
        self.assertIn('max_guest', place1_dict)
        self.assertIn('price_by_night', place1_dict)
        self.assertIn('latitude', place1_dict)
        self.assertIn('longitude', place1_dict)
        self.assertIn('amenity_ids', place1_dict)

        self.assertIsInstance(place1_dict['id'], str)
        self.assertIsInstance(place1_dict['created_at'], str)
        self.assertIsInstance(place1_dict['updated_at'], str)
        self.assertIsInstance(place1_dict['city_id'], str)
        self.assertIsInstance(place1_dict['user_id'], str)
        self.assertIsInstance(place1_dict['name'], str)
        self.assertIsInstance(place1_dict['description'], str)
        self.assertIsInstance(place1_dict['number_rooms'], int)
        self.assertIsInstance(place1_dict['number_bathrooms'], int)
        self.assertIsInstance(place1_dict['max_guest'], int)
        self.assertIsInstance(place1_dict['price_by_night'], int)
        self.assertIsInstance(place1_dict['latitude'], float)
        self.assertIsInstance(place1_dict['longitude'], float)
        self.assertIsInstance(place1_dict['amenity_ids'], list)
        self.assertIsInstance(place1_dict['amenity_ids'][0], str)

        self.assertEqual(place1_dict['id'], self.place1.id)
        self.assertEqual(place1_dict['city_id'], self.place1.city_id)
        self.assertEqual(place1_dict['user_id'], self.place1.user_id)
        self.assertEqual(place1_dict['name'], self.place1.name)
        self.assertEqual(place1_dict['description'], self.place1.description)
        self.assertEqual(
            place1_dict['number_rooms'], self.place1.number_rooms)
        self.assertEqual(
            place1_dict['number_bathrooms'], self.place1.number_bathrooms)
        self.assertEqual(place1_dict['max_guest'], self.place1.max_guest)
        self.assertEqual(
            place1_dict['price_by_night'], self.place1.price_by_night)
        self.assertEqual(place1_dict['latitude'], self.place1.latitude)
        self.assertEqual(place1_dict['longitude'], self.place1.longitude)
        self.assertListEqual(
            place1_dict['amenity_ids'], self.place1.amenity_ids)
        self.assertEqual(place1_dict['__class__'], "Place")

    def test_place_args(self):
        """Test that *args is not used"""
        sample_args = [uuid.uuid4(),
                       "Staff was kind. ENjoyed my stay", uuid.uuid4()]
        my_place = Place(*sample_args)
        self.assertFalse(my_place.id in sample_args)
        self.assertNotEqual(sample_args[1], my_place.description)
        self.assertNotEqual(sample_args[2], my_place.city_id)

    def test_place_kwargs(self):
        """Test that **kwargs is used to instanciate objects"""
        sample_kwargs = {
            'id': str(uuid.uuid4()),
            'city_id': "City." + str(uuid.uuid4()),
            'user_id': "User." + str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(sep="T",
                                                   timespec="microseconds"),
            'name': 'Luxury Apartments',
            'description': 'Bringing luxury to your night stay',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 2,
            'price_by_night': 15000,
            'latitude': 5.342,
            'longitude': 87.42,
            'amenity_ids': ["Amenity." + str(uuid.uuid4()),
                            "Amenity." + str(uuid.uuid4()),
                            "Amenity." + str(uuid.uuid4())],
            '__class__': 'DummyPlaceClass',
        }
        my_place = Place(**sample_kwargs)
        self.assertEqual(sample_kwargs['id'], my_place.id)
        self.assertEqual(sample_kwargs['created_at'],
                         my_place.created_at.isoformat(
                             sep="T", timespec="microseconds"))
        self.assertEqual(sample_kwargs['city_id'], my_place.city_id)
        self.assertEqual(sample_kwargs['user_id'], my_place.user_id)
        self.assertEqual(sample_kwargs['name'], my_place.name)
        self.assertEqual(sample_kwargs['description'], my_place.description)
        self.assertEqual(sample_kwargs['number_rooms'], my_place.number_rooms)
        self.assertEqual(
            sample_kwargs['number_bathrooms'], my_place.number_bathrooms)
        self.assertEqual(sample_kwargs['max_guest'], my_place.max_guest)
        self.assertEqual(
            sample_kwargs['price_by_night'], my_place.price_by_night)
        self.assertEqual(sample_kwargs['latitude'], my_place.latitude)
        self.assertEqual(sample_kwargs['longitude'], my_place.longitude)
        self.assertListEqual(
            sample_kwargs['amenity_ids'], my_place.amenity_ids)
        self.assertEqual(
            sample_kwargs['amenity_ids'][0], my_place.amenity_ids[0])
        self.assertEqual(
            len(sample_kwargs['amenity_ids']), len(my_place.amenity_ids))
        self.assertNotEqual(sample_kwargs['__class__'], my_place.__class__)
        self.assertIsInstance(self.place1.created_at, datetime)

    def test_place_save(self):
        """Test that a `Place` object is saved to file storage"""
        my_place = Place()
        my_place.save()
        self.assertNotEqual(my_place.created_at, my_place.updated_at)
