#!/usr/bin/python3
"""Define a function that checks exact class instance match."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False."""
    return type(obj) is a_class
