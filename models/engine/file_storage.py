#!/usr/bin/python3
"""
This module will define our storage system for our model objects
It will use json to persistently store our objects to a file for
later use when the program is used or to be used in other program
"""
import json


class FileStorage:
    """
    Class which converts our model objects to a json str representation
    Class attrs:
        __file_path: path to the json file
        __objects: a dictionary which will contain all objects created
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the objects dictionary containing all the objects created
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Updates the objects dictionary with the new object
        """
        FileStorage.__objects[
                "{}.{}".format(obj.to_dict()['__class__'], obj.id)] = obj

    def save(self):
        """
        Serialises the dictionary objects to a json file
        """
        json_obj = json.dumps(
                FileStorage.__objects, default=lambda o: o.to_dict())
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json_obj)

    def reload(self):
        """
        Deserialises a json to class dictionary objects if json file exists
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.place import Place
                from models.amenity import Amenity
                from models.review import Review
                temp = dict()
                temp = json.loads(f.read())
                for key, value in temp.items():
                    child = key.split('.')[0]
                    if child == "User":
                        FileStorage.__objects[key] = User(**value)
                    elif child == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif child == "State":
                        FileStorage.__objects[key] = State(**value)
                    elif child == "City":
                        FileStorage.__objects[key] = City(**value)
                    elif child == "Place":
                        FileStorage.__objects[key] = Place(**value)
                    elif child == "Amenity":
                        FileStorage.__objects[key] = Amenity(**value)
                    elif child == "Review":
                        FileStorage.__objects[key] = Review(**value)
        except Exception:
            FileStorage.__objects = {}
