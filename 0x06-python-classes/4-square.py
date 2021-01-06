#!/usr/bin/python3
"""Creating a class"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """initializing size as private attribute"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """gets the value of the attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """updates the attribute size"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """defining a method to calc the square area"""
        return self.__size ** 2
