#!/usr/bin/python3
"""Module that defines read_file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print it to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
