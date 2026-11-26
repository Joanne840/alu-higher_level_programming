#!/usr/bin/python3
"""Define a function that appends a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append text to filename (UTF-8) and return added character count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
