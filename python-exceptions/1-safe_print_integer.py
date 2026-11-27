#!/usr/bin/python3
"""Safely print an integer using {:d}.format() without using type()."""


def safe_print_integer(value):
    """Print value if it is an integer and return True, else False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
