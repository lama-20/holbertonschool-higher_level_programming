#!/usr/bin/python3
"""Module that defines Square."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initialize Square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square area."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
