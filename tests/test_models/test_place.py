#!/usr/bin/python3

"""
Module for test Place class
"""

import unittest
import json
import pep8
import datetime

from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
	"""
	Test State class implementation
	"""

    def test_class(self):
        """
	Validate the types of the attributes an class
	"""

        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Place, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Place.city_id, str)
            self.assertIsInstance(Place.user_id, str)
            self.assertIsInstance(Place.name, str)
            self.assertIsInstance(Place.description, str)
            self.assertIsInstance(Place.number_rooms, int)
            self.assertIsInstance(Place.number_bathrooms, int)
            self.assertIsInstance(Place.max_guest, int)
            self.assertIsInstance(Place.price_by_night, int)
            self.assertIsInstance(Place.latitude, float)
            self.assertIsInstance(Place.longitude, float)
            self.assertIsInstance(Place.amenity_ids, list)


    def test_str_method(self):
	"""
	Test str method
	"""

        place = Place()
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)


    def test_to_dict_method(self):
	"""
	Test to_dict_method of place class
	"""

        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], place.id)
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)


    def test_doc_module(self):
        """
	Module documentation
	"""
        doc = Place.__doc__
        self.assertGreater(len(doc), 1)


    def test_doc_constructor(self):
        """
	Constructor documentation
	"""

        doc = Place.__init__.__doc__
        self.assertGreater(len(doc), 1)


    def test_pep8_conformance_test_place(self):
        """
	Test that tests/test_models/test_place.py conforms to PEP8.
	"""

        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
