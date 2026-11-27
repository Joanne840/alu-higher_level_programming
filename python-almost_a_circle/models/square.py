#!/usr/bin/python3
"""Module that defines the Square class inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square as a specialized Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set and validate size on width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the formatted string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Update attributes using positional args or keyword kwargs."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for idx, val in enumerate(args):
                if idx < len(attrs):
                    setattr(self, attrs[idx], val)
        else:
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
