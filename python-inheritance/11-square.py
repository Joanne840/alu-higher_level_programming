#!/usr/bin/python3
"""Define a Square class with custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square geometry class with area and [Square] string format."""

    def __init__(self, size):
        """Initialize a Square with private size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
