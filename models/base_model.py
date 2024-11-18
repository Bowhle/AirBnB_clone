#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Base model class for other models."""

    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def save(self):
        """Updates updated_at and saves the object."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys and values of the instance."""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """This will print a string representation of the base model."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    @classmethod
    def all(cls):
        """Returns a list of all instances of the class."""
        all_instances = []
        for key, obj in models.storage.all().items():
            if isinstance(obj, cls):
                all_instances.append(str(obj))
        return all_instances
