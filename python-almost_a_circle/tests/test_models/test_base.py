#!/usr/bin/python3
"""Unit tests for the Base class."""
import json
import os
import sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test suite for Base class behavior and JSON serialization."""

    def setUp(self):
        """Reset Base counter and remove temporary JSON files."""
        Base._Base__nb_objects = 0
        for name in ["Base.json", "Rectangle.json", "Square.json"]:
            if os.path.exists(name):
                os.remove(name)

    def tearDown(self):
        """Clean up temporary JSON files after each test."""
        for name in ["Base.json", "Rectangle.json", "Square.json"]:
            if os.path.exists(name):
                os.remove(name)

    def test_id_assignment(self):
        """Test automatic and explicit ID assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base(89)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 89)
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test to_json_string with None, empty list, and dictionaries."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        dicts = [{"id": 1, "width": 4, "height": 2, "x": 0, "y": 0}]
        raw = Base.to_json_string(dicts)
        self.assertIsInstance(raw, str)
        self.assertEqual(json.loads(raw), dicts)

    def test_from_json_string(self):
        """Test from_json_string with None, empty string, and valid JSON."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        parsed = Base.from_json_string('[{"id": 5, "size": 3}]')
        self.assertEqual(parsed, [{"id": 5, "size": 3}])

    def test_save_and_load_from_file(self):
        """Test saving and loading Rectangle and Square instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        loaded_r = Rectangle.load_from_file()
        self.assertEqual(len(loaded_r), 2)
        self.assertEqual(str(loaded_r[0]), str(r1))
        self.assertEqual(str(loaded_r[1]), str(r2))
        self.assertIsNot(loaded_r[0], r1)

        s1 = Square(5, 1, 2, 3)
        Square.save_to_file([s1])
        loaded_s = Square.load_from_file()
        self.assertEqual(len(loaded_s), 1)
        self.assertEqual(str(loaded_s[0]), str(s1))

    def test_save_none_and_missing_file(self):
        """Test saving None writes empty JSON list and missing file returns []."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_create(self):
        """Test creating Rectangle and Square instances from dictionaries."""
        r = Rectangle.create(
            **{"id": 12, "width": 3, "height": 6, "x": 1, "y": 2}
        )
        self.assertEqual(str(r), "[Rectangle] (12) 1/2 - 3/6")
        s = Square.create(**{"id": 15, "size": 4, "x": 2, "y": 1})
        self.assertEqual(str(s), "[Square] (15) 2/1 - 4")
