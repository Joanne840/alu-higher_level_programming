#!/usr/bin/python3
"""Return a new dictionary with all integer values multiplied by 2."""


def multiply_by_2(a_dictionary):
    """Return a new dict with each value in a_dictionary doubled."""
    return {key: val * 2 for key, val in a_dictionary.items()}
