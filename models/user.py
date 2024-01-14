#!/usr/bin/python3
""" User class that inherits from"""


from models.base_model import BaseModel


class User(BaseModel):
    """User information class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
