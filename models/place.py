#!/usr/bin/python3

"""Place module

    Contains a Place class that represents a real place
    e.g. an apartment, room etc.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class

        Attributes:
            city_id (str): ID of a city
            user_id (str): ID of a user
            name (str): Name of a place
            description (str): details about a place
            number_rooms (int): Number of rooms
            number_bathrooms (int): Number of bathrooms
            max_guest (int): The maximum amount of guests allowed
            price_by_night (int): The price of a night stay in a place
            latitude (float): Latitude coordinates of a place
            longitude (float): Longitude coordinates of a place
            amenity_ids (list): A list of amenities a place has; `amenity_id[]`
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
        """Initialize a place instance"""
        super().__init__(*args, **kwargs)
