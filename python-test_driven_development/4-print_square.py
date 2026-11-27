#!/usr/bin/python3
"""Module that provides a function to print a square with '#' characters."""


def print_square(size):
    """Print a square of size using '#' characters."""
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
