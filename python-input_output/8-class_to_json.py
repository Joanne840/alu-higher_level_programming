#!/usr/bin/python3
"""Define a function that returns the dictionary description of an object."""


def class_to_json(obj):
    """Return a simple dictionary description of obj for JSON serialization."""
    return obj.__dict__.copy()
