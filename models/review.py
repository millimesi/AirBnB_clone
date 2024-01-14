#!/usr/bin/python3
""" Review class that inherits from"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review information class"""
    place_id = ""
    user_id = ""
    text = ""
