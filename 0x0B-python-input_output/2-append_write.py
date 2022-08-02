#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Return:
        number of characters appended."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
