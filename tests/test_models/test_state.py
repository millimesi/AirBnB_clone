#!/usr/bin/python3

"""
Module for test State class
"""

import unittest
import json
import pep8
import datetime

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
	"""
	Test State class implementation
	"""

   def test_class(self):
        """
	Validate the types of the attributes an class
	"""

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)

	with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        
   def test_attributes_inherited(self):
	"""
	Test for inherited attributes
	"""

        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))


    def test_str_method(self):
	"""
	Test the str method of state class
	"""

        state = State()
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)


    def test_to_dict_method(self):
	"""
	Test the to_dict_method of state class
	"""

        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], state.id)
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)


    def test_doc_module(self):
        """
	Module documentation
	"""

        doc = State.__doc__
        self.assertGreater(len(doc), 1)


   def test_doc_constructor(self):
        """
	Constructor documentation
	"""

        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)


    def test_pep8_conformance_test_state(self):
        """
	Test that tests/test_models/test_state.py conforms to PEP8.
	"""

        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
