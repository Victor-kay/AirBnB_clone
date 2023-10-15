#!/usr/bin/python3

"""File storage module

Contains a filestorage class that
serializes/deserializes data to/from JSON files
"""
import json


class FileStorage:
    """Manage application data storage

        Attributes:
            __file_path (str): Path to JSON file
            __objects (object): Stores all created objects
    """

    __file_path = "file.json"
    __objects = {}

    # def __init__(self):
    #     """Initialize a File storage instance"""
    def all(self):
        """Returns all objects created"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object in `__objects`"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialized `__objects` to the JSON file"""
        with open(FileStorage.__file_path,
                  mode="w", encoding="utf-8") as file:
            data_dict = {}
            for key, value in FileStorage.__objects.items():
                data_dict[key] = value.to_dict()
            json.dump(data_dict, file)

    def reload(self):
        """Deserialize a JSON file to `__objects`"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "Review": Review,
            "State": State,
            "City": City,
            "Amenity": Amenity
        }
        try:
            with open(FileStorage.__file_path, "r",
                      encoding="utf-8") as file:
                data_dict = json.load(file)
                for key, value in data_dict.items():
                    FileStorage.__objects[key] = classes[value["__class__"]](
                        **value)
        except FileNotFoundError:
            pass
