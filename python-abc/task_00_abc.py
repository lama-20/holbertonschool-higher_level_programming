#!/usr/bin/env python3
"""Module that defines abstract Animal class."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal class."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Return dog's sound."""
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Return cat's sound."""
        return "Meow"
