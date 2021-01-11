#!/usr/bin/python3
"""Creating a new class Rectangle"""


class Rectangle:
    """Defines a Rectangle class"""
    def __init__(self, width=0, heigth=0):
        self.__heigth = heigth
        self.__width = width

    @property
    def heigth(self):
        """gets the heigth of the rectangle"""
        return self.__heigth

    @heigth.setter
    def heigth(self, heigth):
        """Sets the heigth of the rectangle"""
        if type(heigth) != int:
            raise TypeError("height must be an integer")
        if heigth < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = heigth

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
