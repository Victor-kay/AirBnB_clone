#!/usr/bin/python3

"""Amenity module

    Contains a Amenity class that represents an amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class

        Attributes:
            name (str): Name of the amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the amenity instance"""
        super().__init__(*args, **kwargs)
