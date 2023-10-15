#!/usr/bin/python3

"""Review module

    Contains a Review class that represents a review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class

        Attributes:
            user_id (str): ID of a user
            place_id (str): ID of a place
            text (str): A review about a place
    """

    user_id = ""
    place_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize the amenity instance"""
        super().__init__(*args, **kwargs)
