#!/usr/bin/python3
""" New module """


def read_file(filename=""):
    """ Reads a text file and prints it to stdout """
    f = open(filename, 'r')
    print(f.read())
