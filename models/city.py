#!/usr/bin/python3

"""City module

    Contains a City class that represents a real city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class

        Attributes:
            state_id (str): The unique id of a state
            name (str): Name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the city instance"""
        super().__init__(*args, **kwargs)
