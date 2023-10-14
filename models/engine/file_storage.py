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

    __file_path = "data.json"
    __objects = {}

    # def __init__(self):
    #     """Initialize a File storage instance"""
    def all(self):
        """Returns all objects created"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object in `__objects`"""
        FileStorage.__objects[
            obj.__class__.__name__
            + "."
            + obj.id] = obj.to_dict()

    def save(self):
        """Serialized `__objects` to the JSON file"""
        with open(FileStorage.__file_path,
                  mode="w", encoding="utf-8") as file:
            obj_json = json.dumps(FileStorage.__objects)
            file.write(obj_json)

    def reload(self):
        """Deserialize a JSON file to `__objects`"""
        try:
            with open(FileStorage.__file_path,
                      mode="r",
                      encoding="utf-8") as file:
                objects = json.loads(file.read())
                FileStorage.__objects = objects
        except FileNotFoundError:
            pass
