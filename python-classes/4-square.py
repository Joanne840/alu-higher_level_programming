#!/usr/bin/python3
"""This module defines a Square class with property getter and setter for size."""


class Square:
    """This class represents a square with a managed size property."""

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
