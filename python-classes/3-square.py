#!/usr/bin/python3
"""This module defines a Square class with size validation and area method."""


class Square:
    """This class represents a square and computes its area."""

    def __init__(self, size=0):
        """Initialize a new Square instance with optional validated size."""
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
