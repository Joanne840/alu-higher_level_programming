#!/usr/bin/python3
"""Delete a key from a dictionary if it exists."""


def simple_delete(a_dictionary, key=""):
    """Remove key from a_dictionary if present and return it."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
