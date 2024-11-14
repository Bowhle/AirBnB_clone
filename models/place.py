#!/usr/bin/python3
""" Place class for the AirBnB clone project """
from models.base_model import BaseModel

class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    city_id = ""  # empty string for city_id
    user_id = ""  # empty string for user_id
    name = ""  # empty string for place name
    description = ""  # empty string for description
    number_rooms = 0  # integer for number of rooms
    number_bathrooms = 0  # integer for number of bathrooms
    max_guest = 0  # integer for maximum guests
    price_by_night = 0  # integer for price per night
    latitude = 0.0  # float for latitude
    longitude = 0.0  # float for longitude
    amenity_ids = []  # list of amenity_ids
