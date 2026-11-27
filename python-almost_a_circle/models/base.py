#!/usr/bin/python3
"""Module that defines the Base class for managing object IDs and JSON I/O."""
import json
import os


class Base:
    """Base class for models in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a given or auto-incremented id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to <Class>.json."""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            dicts = []
        else:
            dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(dicts)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        if hasattr(dummy, "update"):
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class>.json."""
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        dicts = cls.from_json_string(content)
        return [cls.create(**d) for d in dicts]
