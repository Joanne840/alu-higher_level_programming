#!/usr/bin/python3
"""Define a function that returns the JSON string of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of my_obj."""
    return json.dumps(my_obj)
