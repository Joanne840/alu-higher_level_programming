#!/usr/bin/python3
"""Convert a Roman numeral string to an integer."""


def roman_to_int(roman_string):
    """Return the integer value of roman_string, or 0 if invalid."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    total = 0
    length = len(roman_string)

    for i in range(length):
        curr = values.get(roman_string[i], 0)
        if i + 1 < length:
            nxt = values.get(roman_string[i + 1], 0)
            if curr < nxt:
                total -= curr
                continue
        total += curr

    return total
