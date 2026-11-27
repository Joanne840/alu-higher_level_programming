#!/usr/bin/python3
"""Compute the square value of all integers in a 2D matrix."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with each element squared."""
    return [[val ** 2 for val in row] for row in matrix]
