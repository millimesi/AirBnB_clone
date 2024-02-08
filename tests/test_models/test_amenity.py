#!/usr/bin/python3

"""
Module for test Amenity class
"""

import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
	"""
	Test Amenity class implementation
	"""

   def test_class(self):
	"""
	Validate the types of the attributes in a class
	"""
	
	with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)
	
    def test_inheritance(self):
	"""
	Test inheritance of Amenity class
	"""

        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))


    def test_attributes_inherited(self):
	"""
	Test inherited attributes
	"""
	
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
    

    def test_str_method(self):
	"""
	Test str method
	"""

        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)


    def test_to_dict_method(self):
	"""
	Test to_dict_method for amenity class
	"""

        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)


    def test_doc_module(self):
        """
	Module documentation
	"""

        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

	
	def test_doc_constructor(self):
        """
	Constructor documentation
	"""

        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)


    def test_pep8_conformance_test_amenity(self):
        """
	Test that tests/test_models/test_amenity.py conforms to PEP8.
	"""

        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
