#!/usr/bin/python3
"""Define a function that writes an object as JSON to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Write my_obj to filename using its JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
