#!/usr/bin/python3
"""Creting a class"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        self.__size = size
        """Initializing size as private attribute"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        """Check if size is not an integer"""

        if size < 0:
            raise ValueError("size must be >= 0")
        """Checks id size if lower than zero"""
