#!/usr/bin/python3
"""This module defines a Square class that can print itself using #."""


class Square:
    """This class represents a square with area and printing support."""

    def __init__(self, size=0):
        """Initialize a new Square instance with optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the private size attribute of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute after validating type and value."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' characters to stdout."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
