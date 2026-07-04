#!/usr/bin/python3
"""Module that defines write_file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
