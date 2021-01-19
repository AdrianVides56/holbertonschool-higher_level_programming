#!/usr/bin/python3
"""Creating a new function"""


def lookup(obj):
    """
    Return the list of available attributes
    and methods of an object
    """
    return list(dir(obj))
