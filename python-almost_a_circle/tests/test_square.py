#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for Square functionality and validation."""

    def setUp(self):
        """Reset Base counter before each test."""
        Base._Base__nb_objects = 0

    def test_square_str_and_size(self):
        """Test Square creation, __str__, and size getter/setter."""
        s = Square(5, 2, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 2/3 - 5")
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(str(s), "[Square] (7) 2/3 - 10")

    def test_square_validation(self):
        """Test invalid size/x/y values raise expected errors."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(4, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(4, 0, -2)

    def test_square_update_and_dict(self):
        """Test Square update() and to_dictionary()."""
        s = Square(5, 0, 0, 1)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (10) 3/1 - 7")
        self.assertEqual(
            s.to_dictionary(),
            {"id": 10, "size": 7, "x": 3, "y": 1},
        )
