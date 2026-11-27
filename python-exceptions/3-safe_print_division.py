#!/usr/bin/python3
"""Divide two integers and print the result inside a finally block."""


def safe_print_division(a, b):
    """Divide a by b, print 'Inside result: <val>', and return result/None."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
