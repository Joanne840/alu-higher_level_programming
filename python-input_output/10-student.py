#!/usr/bin/python3
"""Define a Student class with filtered JSON serialization."""


class Student:
    """Represent a student with optional attribute filtering in to_json."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict of attributes, filtered by attrs if list of strings."""
        if isinstance(attrs, list) and all(
            isinstance(item, str) for item in attrs
        ):
            return {
                k: v for k, v in self.__dict__.items() if k in attrs
            }
        return self.__dict__.copy()
