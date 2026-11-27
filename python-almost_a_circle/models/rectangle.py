#!/usr/bin/python3
"""Module that defines the Rectangle class inheriting from Base."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle with width, height, x, and y attributes."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate and set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate and set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve the x offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Validate and set the x offset of the rectangle."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve the y offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Validate and set the y offset of the rectangle."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle in stdout using '#' with x and y offsets."""
        if self.__y > 0:
            print("\n" * (self.__y - 1))
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return the formatted string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Update rectangle attributes from positional args or keyword args."""
        attrs = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for idx, val in enumerate(args):
                if idx < len(attrs):
                    setattr(self, attrs[idx], val)
        else:
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
