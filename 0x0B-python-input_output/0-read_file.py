#!/usr/bin/python3
""" New module """


def read_file(filename=""):
    """ Reads a text file and prints it to stdout """
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end="")
