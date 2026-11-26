#!/usr/bin/python3
"""This module defines a Rectangle class that announces instance deletion."""


class Rectangle:
    """This class represents a rectangle and prints a message on deletion."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the private width attribute of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private width attribute after validating type and value."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the private height attribute of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the private height attribute after validating type and value."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if any side is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a visual representation of the rectangle using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        row = "#" * self.__width
        return "\n".join(row for _ in range(self.__height))

    def __repr__(self):
        """Return an official string representation to recreate the instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a farewell message when the rectangle instance is deleted."""
        print("Bye rectangle...")
