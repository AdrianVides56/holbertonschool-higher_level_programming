#!/usr/bin/python3
""" Creating a function"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class
    else returns False
    """
    return bool(type(obj) is a_class)
