#!/usr/bin/python3
"""Print a dictionary ordered by first-level keys."""


def print_sorted_dictionary(a_dictionary):
    """Print key: value pairs sorted alphabetically by key."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
