#!/usr/bin/python3
"""Replace all occurrences of an element in a new list."""


def search_replace(my_list, search, replace):
    """Return a new list with search elements replaced by replace."""
    return [replace if item == search else item for item in my_list]
