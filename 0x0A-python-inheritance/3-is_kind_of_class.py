#!/usr/bin/python3
""" Creating a function"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or if obj\
    is an instance of a class that inhereted from
    else retuturns False
    """
    return bool(isinstance(obj, a_class))
