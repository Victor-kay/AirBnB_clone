#!/usr/bin/python3

"""Module for the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class

        Attributes:
            name (str): Name of the state
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiate the state class"""
        super().__init__(*args, **kwargs)
