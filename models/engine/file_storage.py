#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes and deserializes objects to and from JSON."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects."""
        return self.__objects

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
                    elif class_name == "State":
                        obj = State(**value)
                    elif class_name == "City":
                        obj = City(**value)
                    elif class_name == "Amenity":
                        obj = Amenity(**value)
                    elif class_name == "Place":
                        obj = Place(**value)
                    elif class_name == "Review":
                        obj = Review(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
