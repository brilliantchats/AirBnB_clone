#!/usr/bin/python3
"""
Defines the Amenity class for the site
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines the Amenity class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialises the class"""
        super().__init__(*args, **kwargs)
