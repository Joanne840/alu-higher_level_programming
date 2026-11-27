#!/usr/bin/python3
"""Module that provides a function to indent text after '.', '?', and ':'."""


def text_indentation(text):
    """Print text with two new lines after '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for ch in text:
        if ch == "\n":
            continue
        line += ch
        if ch in ".?:":
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip(), end="")
