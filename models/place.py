#!/usr/bin/python3
"""
Defines a class Place that will inherit from BaseModel
"""
from models.base_model import BaseModel
from models.city import City
from models.user import User


class Place(BaseModel):
    """
    Class which inherits from BaseModel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialises the Place class"""
        super().__init__(*args, **kwargs)
