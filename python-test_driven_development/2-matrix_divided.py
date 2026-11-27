#!/usr/bin/python3
"""Module that provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimal places."""
    msg_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_matrix)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_matrix)
        for val in row:
            if not isinstance(val, (int, float)) or isinstance(val, bool):
                raise TypeError(msg_matrix)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(val / div, 2) for val in row] for row in matrix]
