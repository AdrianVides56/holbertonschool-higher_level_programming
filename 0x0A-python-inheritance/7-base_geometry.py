#!/usr/bin/python3
""" Creates a class """


class BaseGeometry:
    """ class """

    def area(self):
        """ Empty method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value < 1:
            raise ValueError(name + " must be greater than 0")
