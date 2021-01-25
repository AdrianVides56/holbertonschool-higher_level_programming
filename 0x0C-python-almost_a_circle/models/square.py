#!/usr/bin/python3
""" Initializes module and import """
from .rectangle import Rectangle


class Square(Rectangle):
    """ Class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Defines initial state of the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns square information """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Gets the size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the square """
        if len(args) > 0:
            for count in range(len(args)):
                if count == 0:  # Updates id
                    self.id = args[0]
                if count == 1:  # Updates size
                    self.size = args[1]
                if count == 2:  # Updates x
                    self.x = args[2]
                if count == 3:  # Updates y
                    self.y = args[3]
        else:
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "id" in kwargs:
                self.id = kwargs["id"]

    def to_dictionary(self):
        """ Returns the dictionary representation of a square """
        return dict({"id": self.id, "size": self.size,
                     "x": self.x, "y": self.y})
