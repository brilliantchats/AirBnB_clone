#!/usr/bin/python3
"""
Defines a class, City, which defines a city like the real world
"""
from models.base_model import BaseModel
from models.state import State
from models import storage


class City(BaseModel):
    """
    A class to define an actual city on our site
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialises the City class"""
        super().__init__(*args, **kwargs)
