#!/usr/bin/python3
"""
Defines a base class which will inherited by other subclasses
within this project
Defines common attributes and methods common to all objects of this project
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    Defines a base class for all objects to inherit
    Will define common methods to all other objects
    """
    def __init__(self, *args, **kwargs):
        """
        Initialises an object based on the parent class
        Will set public attributes: id, created_at and updated_at
        Arguments:
            args: optional positional arguments
            kwargs: optional keyword arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the object
        Adds a key __class__ with the name of the class
        Adds created_at and updated_at in ISO string format
        """
        final_dict = dict()
        for k, v in self.__dict__.items():
            final_dict[k] = v
        final_dict['__class__'] = "BaseModel"
        final_dict['created_at'] = self.created_at.isoformat()
        final_dict['updated_at'] = self.updated_at.isoformat()
        return final_dict

    def __str__(self):
        """
        String representation of the object
        """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance variable, updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        storage.save()
