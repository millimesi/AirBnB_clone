#!/usr/bin/python3

"""
Module for test Review class
"""

import unittest
import json
import pep8
import datetime

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
	"""
	Test Review class
	"""

    def test_class(self):
	"""
	Validate the types of the attributes an class
	"""

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)
	
	with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))


    def test_attributes_inherited(self):
	"""
	Test inherited attributes
	"""

        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))


    def test_str_method(self):
	"""
	Test str methof of review class
	"""

        review = Review()
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected_str)


    def test_to_dict_method(self):
	"""
	Test to_dict_method of class review
	"""

        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], review.id)
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)


    def test_doc_module(self):
        """
	Module documentation
	"""

        doc = Review.__doc__
        self.assertGreater(len(doc), 1)


    def test_doc_constructor(self):
        """
	Constructor documentation
	"""

        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)


    def test_pep8_conformance_test_review(self):
        """
	Test that tests/test_models/test_review.py conforms to PEP8.
	"""

        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
