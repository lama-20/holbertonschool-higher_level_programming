#!/usr/bin/python3
"""Module that defines append_write."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
