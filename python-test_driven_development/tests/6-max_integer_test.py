#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when maximum value is at the start."""
        self.assertEqual(max_integer([10, 5, 2, 1]), 10)

    def test_max_at_end(self):
        """Test when maximum value is at the end."""
        self.assertEqual(max_integer([1, 5, 2, 10]), 10)

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-10, -3, -50, -1]), -1)

    def test_mixed_positive_and_negative(self):
        """Test a list with both negative and positive integers."""
        self.assertEqual(max_integer([-5, 0, 12, -1, 7]), 12)

    def test_duplicate_max(self):
        """Test a list where the maximum appears multiple times."""
        self.assertEqual(max_integer([7, 2, 7, 3]), 7)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Test calling max_integer with no arguments."""
        self.assertIsNone(max_integer())
