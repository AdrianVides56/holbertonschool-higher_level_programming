#!/usr/bin/python3
""" Initializes module and import Base """
from .base import Base


class Rectangle(Base):
    """ Class that inherits from super class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initial state of new instances"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Gets the width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets the width """
        self.__width = width

    @property
    def height(self):
        """ Gets the height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the height """
        self.__height = height

    @property
    def x(self):
        """ Gets x """
        return self.__x

    @width.setter
    def x(self, x):
        """ Sets x """
        self.__x = x

    @property
    def y(self):
        """ Gets y """
        return self.__y

    @width.setter
    def y(self, y):
        """ Sets the y """
        self.__y = y
