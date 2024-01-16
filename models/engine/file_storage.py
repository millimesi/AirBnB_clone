#!/usr/bin/python3
"""
serializes instances to a JSON file and
deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """ serialization and Desrialization"""
    def __init__(self):
    self.__file_path = "file.json"
    self.__objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the
        JSON file (path: __file_path)"""
        objects = {}
        for key in self.__objects:
            objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(objects, file)

    def reload(self):
        """deserializes the JSON file to
        __objects (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, "r") as file:
                loaded_obj = json.load(file)
                for key, value in loaded_obj.items():
                    class_name, obj_id = key.split(".")
                    class_creater = eval(class_name)
                    reloaded_obj = class_creater(**value)
                    self.__objects[key] = reloaded_obj
        except FileNotFoundError:
            pass
