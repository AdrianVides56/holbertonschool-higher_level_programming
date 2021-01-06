#!/usr/bin/python3
"""Creating a class"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        self.__size = size
        """initializing size as private attribute"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        """Check if size is not an integer"""

        if size < 0:
            raise ValueError("size must be >= 0")
        """Checks if size is lower than zero"""

    def area(self):
        """defining a method to calc the square area"""
        return self.__size ** 2
