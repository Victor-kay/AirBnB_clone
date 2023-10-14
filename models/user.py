#!/usr/bin/python3

"""User Module

    Contains the User class that represents a user
    in the application
"""
from models.base_model import BaseModel


class User(BaseModel):
    """The user model class"""

    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self):
        """Initialize a user instance"""
        super().__init__()
