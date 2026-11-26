#!/usr/bin/python3
"""Define a function that checks strict subclass inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
