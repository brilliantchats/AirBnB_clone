#!/usr/bin/python3
"""
Defines a class User that will inherit from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class which inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialises the User class"""
        super().__init__(*args, **kwargs)
