#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle functionality and validation."""

    def setUp(self):
        """Reset Base counter before each test."""
        Base._Base__nb_objects = 0

    def test_instantiation_and_str(self):
        """Test Rectangle creation, defaults, and __str__."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_validation_errors(self):
        """Test TypeError and ValueError on invalid attributes."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, [1])
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 3, 0, -1)

    def test_area_and_display(self):
        """Test area() and display() with x and y offsets."""
        r = Rectangle(2, 3, 2, 2, 10)
        self.assertEqual(r.area(), 6)
        buf = io.StringIO()
        with redirect_stdout(buf):
            r.display()
        self.assertEqual(buf.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_update_args_and_kwargs(self):
        """Test update() with *args and **kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")
        r.update(99, height=7)
        self.assertEqual(str(r), "[Rectangle] (99) 4/5 - 2/3")
        r.update(x=1, y=2, width=8, height=9, id=50)
        self.assertEqual(str(r), "[Rectangle] (50) 1/2 - 8/9")

    def test_to_dictionary(self):
        """Test to_dictionary() keys and values."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(
            r.to_dictionary(),
            {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9},
        )
