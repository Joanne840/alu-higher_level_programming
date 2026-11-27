#!/usr/bin/python3
"""Unit tests for the Base class."""
import io
import json
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test suite for Base functionality."""

    def setUp(self):
        """Reset Base counter and clean up test JSON files."""
        Base._Base__nb_objects = 0
        for fname in ["Base.json", "Rectangle.json", "Square.json"]:
            if os.path.exists(fname):
                os.remove(fname)

    def tearDown(self):
        """Clean up test JSON files after each test."""
        for fname in ["Base.json", "Rectangle.json", "Square.json"]:
            if os.path.exists(fname):
                os.remove(fname)

    def test_auto_id(self):
        """Test automatic sequential ID assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id_and_counter(self):
        """Test custom IDs do not increment auto counter."""
        b1 = Base()
        b2 = Base(42)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 42)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """Test JSON string conversion for empty, None, and dicts."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]
        js = Base.to_json_string(d)
        self.assertIsInstance(js, str)
        self.assertEqual(json.loads(js), d)

    def test_from_json_string(self):
        """Test parsing JSON string back into list of dicts."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        res = Base.from_json_string('[{"id": 7, "size": 5}]')
        self.assertEqual(res, [{"id": 7, "size": 5}])

    def test_save_and_load_rectangle(self):
        """Test saving and loading Rectangle instances to/from file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))
        self.assertIsNot(loaded[0], r1)

    def test_save_none_and_load_missing_file(self):
        """Test save_to_file(None) and load_from_file when file missing."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_create_rectangle_and_square(self):
        """Test creating instances from dictionaries."""
        r = Rectangle.create(**{"id": 89, "width": 3, "height": 4, "x": 1, "y": 2})
        self.assertEqual(str(r), "[Rectangle] (89) 1/2 - 3/4")
        s = Square.create(**{"id": 99, "size": 6, "x": 2, "y": 3})
        self.assertEqual(str(s), "[Square] (99) 2/3 - 6")

    def test_stdout_capture(self):
        """Test display output using redirect_stdout."""
        buf = io.StringIO()
        r = Rectangle(2, 1, 1, 0, 5)
        with redirect_stdout(buf):
            r.display()
        self.assertEqual(buf.getvalue(), " ##\n")
