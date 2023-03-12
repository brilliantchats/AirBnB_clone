#!/usr/bin/python3
"""
Defines a class Review that will inherit from BaseModel
"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """
    Class which inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialises the Review class"""
        super().__init__(*args, **kwargs)
