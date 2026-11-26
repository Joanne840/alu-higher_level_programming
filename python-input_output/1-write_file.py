#!/usr/bin/python3
"""Define a function that writes a string to a UTF-8 text file."""


def write_file(filename="", text=""):
    """Write text to filename (UTF-8) and return character count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
