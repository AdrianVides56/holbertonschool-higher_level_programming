#!/usr/bin/python3
""" Create a subclass"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Impoting a module """


class Rectangle(BaseGeometry):
    """
    New subclass Rectangle
    Inherits from supeclass BaseGeometry
    """
    def __init__(self, width, height):
        """ Defines the intial state of the new instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
