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

    @property
    def height(self):
        """ Gets the height """
        return self.__height

    @property
    def x(self):
        """ Gets x """
        return self.__x

    @property
    def y(self):
        """ Gets y """
        return self.__y

    @width.setter
    def width(self, value):
        """ Sets the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ Sets x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ Sets the y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle with '#' """
        for a in range(self.__y):
            print()
        for a in range(self.__height):
            print(' ' * (self.__x) + '#' * self.__width)

    def __str__(self):
        """ Returns rectangle information"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Updates the rectangle """
        if len(args) > 0:
            for count in range(len(args)):
                if count == 0:  # Updates id
                    self.id = args[0]
                if count == 1:  # Updates width
                    self.__width = args[1]
                if count == 2:  # Updates height
                    self.__height = args[2]
                if count == 3:  # Updates x
                    self.__x = args[3]
                if count == 4:  # Updates y
                    self.__y = args[4]
        else:
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
            if "id" in kwargs:
                self.id = kwargs["id"]

    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle """
        return dict({"id": self.id, "width": self.__width,
                     "height": self.__height, "x": self.__x, "y": self.__y})
