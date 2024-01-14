#!/usr/bin/python3
""" Module for class BaseModel- that defines all common
attributes/methods for other classes
"""


from datetime import datetime
import uuid


class BaseModel():
    """ defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ defines the attributes"""
        from models import storage

        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """  returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        ints_dic = self.__dict__.copy()
        ints_dic['created_at'] = self.created_at.isoformat()
        ints_dic['updated_at'] = self.updated_at.isoformat()
        ints_dic['__class__'] = self.__class__.__name__
        return ints_dic
