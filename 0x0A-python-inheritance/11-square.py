#!/usr/bin/python3
""" New module """


Rectangle = __import__('9-rectangle').Rectangle
"""Import Rectangle module"""


class Square(Rectangle):
    """Creates new sublass"""
    def __init__(self, size):
        """Initial values"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """description of the square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
