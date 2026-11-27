#!/usr/bin/python3
"""Return the key with the largest integer value in a dictionary."""


def best_score(a_dictionary):
    """Return the key with the highest score or None if unavailable."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
