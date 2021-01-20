#!/usr/bin/python3
""" Creating a new class """


class MyList(list):
    """ Class that inherits from list """
    def print_sorted(self):
        """ Prints a list in ascending order """
        print(sorted(self))
