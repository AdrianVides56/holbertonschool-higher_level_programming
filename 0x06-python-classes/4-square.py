#!/usr//bin/python3
"""Creating a class"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    """getter"""

    @size.setter
    def size(self, value):
        self.__size = value
        """setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
