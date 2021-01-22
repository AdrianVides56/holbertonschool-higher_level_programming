#!/usr/bin/python3
""" Initializes module """


class Student():
    """ Class """
    def __init__(self, first_name, last_name, age):
        """ Initial state of instances """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary of a Stundent instance """
        return self.__dict__
