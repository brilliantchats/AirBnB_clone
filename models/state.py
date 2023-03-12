#!/usr/bin/python3
"""
Defines a class, State that inherits from BaseModel
Its the prototype to create a State instance
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A class to define a State like in the real world"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialises the State class calling the base class constructor"""
        super().__init__(*args, **kwargs)
