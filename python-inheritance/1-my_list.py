#!/usr/bin/python3
"""Define a MyList class that inherits from list."""


class MyList(list):
    """Subclass of list with a method to print elements in sorted order."""

    def print_sorted(self):
        """Print the list elements sorted in ascending order."""
        print(sorted(self))
