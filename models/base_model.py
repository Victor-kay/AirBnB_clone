#!/usr/bin/python3

"""
Module containing the Base model super class for all models

"""
import json
import uuid
from datetime import datetime


class BaseModel:
    """The Base model class"""

    def __init__(self, *args, **kwargs):
        """Initialize a Base instance

            Args:
                *args: arguments
                *kwargs (dict): Key/value pairs of properties of a Base class
        """
        if args and kwargs or kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                if key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of a class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary containing all keys/values
        of `__dict__` instance and the name of the
        object instance's class
        """
        result_dict = self.__dict__.copy()
        result_dict.update({
            'created_at': self.created_at.isoformat(sep="T",
                                                    timespec="microseconds")
            })
        result_dict.update({
            'updated_at': self.updated_at.isoformat(sep="T",
                                                    timespec="microseconds")
        })
        result_dict['__class__'] = self.__class__.__name__
        return result_dict


if __name__ == "__main__":
    base1 = BaseModel()
    base1.to_dict()
    print()
    print(base1)
    print(BaseModel.__dict__)
