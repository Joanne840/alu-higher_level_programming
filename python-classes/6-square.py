#!/usr/bin/python3
"""This module defines a Square class with size and position coordinates."""


class Square:
    """This class represents a square positioned at (x, y) coordinates."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance with optional size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the private position tuple of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position after verifying it is a tuple of 2 non-negative ints."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or isinstance(value[0], bool)
            or value[0] < 0
            or not isinstance(value[1], int)
            or isinstance(value[1], bool)
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' with horizontal and vertical offsets."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
