#!/usr/bin/python3
"""
Module for test BaseModel class
"""

import os
import re
import json
import uuid
import unittest
import pep8

from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test for BaseModel class
    """

	def setUp(self):
        """
	Set up the test environment
	"""

        self.test_storage_file = 'test_storage.json'
        os.environ['HBNB_ENV'] = 'test'
        os.environ['HBNB_STORAGE_FILE'] = self.test_storage_file
	
	def tearDown(self):
        """
	Tear down the test environment
	Remove the temporary storage file after the tests
	"""
      
        if os.path.exists(self.test_storage_file):
            os.remove(self.test_storage_file)

	def test_init(self):
        """
	Test the __init__ method of BaseModel
	"""

        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.id, str)

	def test_string_representation(self):
        """
	Test the magic method str
	"""

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        id_model = my_model.id

        expected = '[BaseModel] ({}) {}'\
                   .format(id_model, my_model.__dict__)
        self.assertEqual(str(my_model), expected)

    	def test_file_save(self):
        """
	Test that info is saved to file
	"""

        b3 = BaseModel()
        b3.save()
        with open("file.json", 'r') as f:
            self.assertIn(b3.id, f.read())

	def test_to_dict(self):
        """
	Test the to_dict method of BaseModel
	"""

        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

	def test_to_dict_isoformat(self):
        """
	Test the to_dict method of BaseModel with isoformat
	"""

        model = BaseModel()
        model_dict = model.to_dict()

        created_at_iso = model.created_at.isoformat()
        updated_at_iso = model.updated_at.isoformat()

        self.assertEqual(model_dict['created_at'], created_at_iso)
        self.assertEqual(model_dict['updated_at'], updated_at_iso)

	def test_save_after_init(self):
        """
	Test the save method of BaseModel after __init__
	"""

        model = BaseModel()
        model_id = model.id
        model.save()

        # Load a new instance from the storage and check if the id matches
        new_model = BaseModel(id=model_id)
        self.assertEqual(new_model.id, model_id)

    def test_doc_module(self):
        """
	Module documentation
	"""

        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """
	Test that models/base_model.py conforms to PEP8.
	"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        """
	Test that tests/test_models/test_base_model.py conforms to PEP8.
	"""

        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
	Constructor documentation
	"""

        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_first_task(self):
        """
	Test creation of class and to_dict
	"""

        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
        }
        my_model_json = my_model.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_base_types(self):
        """
	Testing dict model
	"""

        second_model = BaseModel()
        self.assertIs(type(second_model), BaseModel)
        second_model.name = "Andres"
        second_model.my_number = 80
        self.assertEqual(second_model.name, "Andres")
        self.assertEqual(second_model.my_number, 80)
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime
            }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model.__dict__)
                self.assertIs(type(second_model.__dict__[key]), value)

    def test_uuid(self):
        """
	testing differents uuid
	"""

        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_model(self):
        """
	testing datetime base model
	"""

        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_3.updated_at)
        self.assertNotEqual(model_3.created_at, model_4.created_at)

    def test_constructor_kwargs(self):
        """
	Test constructor that has kwargs as attributes values
	"""

        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        json_attributes = obj.to_dict()

        obj2 = BaseModel(**json_attributes)

        self.assertIsInstance(obj2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(obj, obj2)

if __name__ == '__main__':
    unittest.main()
