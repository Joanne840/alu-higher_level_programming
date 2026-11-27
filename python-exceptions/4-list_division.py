#!/usr/bin/python3
"""Divide element by element across two lists with error handling."""


def list_division(my_list_1, my_list_2, list_length):
    """Return a new list of length list_length with element-wise divisions."""
    result = []
    for i in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(quotient)
    return result
