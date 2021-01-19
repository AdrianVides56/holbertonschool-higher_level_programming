#!/usr/bin/python3
""" Creating a new class """


class MyList(list):
    """ Prints a list in ascending order """
    def print_sorted(self):
        print(sorted(self))
