#!/usr/bin/python3

"""
Module for test City class
"""

import unittest
import json
import pep8
import datetime

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
	"""
	Test City class implementation
	"""

    def test_class(self):
	"""
	Validate the types of the attributes an class
	"""

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)
        
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

     def test_str_method(self):
	"""
	Test str method for city class
	"""

        city = City()
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)        


    def test_to_dict_method(self):
	"""
	Test dictionery method of city class
	"""

        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], city.id)
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)


    def test_doc_module(self):
        """
	Module documentation
	"""

        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_constructor(self):
        """
	Constructor documentation
	"""

        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)


    def test_pep8_conformance_test_city(self):
        """
	Test that tests/test_models/test_city.py conforms to PEP8.
	"""

        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
