#!/usr/bin/python3
import json
""" this is a class that defines file storage"""
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes and deserializes objects to and from JSON."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        ob = str(obj.__class__.__name__)
        FileStorage.__objects[f"{ob}.{obj.id}"] = obj

    def save(self):
        """Serializes the objects to a JSON file."""
        objdic = {}
        for k, v in FileStorage.__objects.items():
            objdic[k] = v.to_dict()

        with open(FileStorage.__file_path, mode='w') as file:
            json.dump(objdic, file)

    def reload(self):
        """Deserializes the JSON file back into objects."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                    elif class_name == "User":
                        obj = User(**value)
                    # Add other classes if needed
                    self.new(obj)
        except FileNotFoundError:
            pass
