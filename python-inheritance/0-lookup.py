#!/usr/bin/python3
"""Define a lookup function for object attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
