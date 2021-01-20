#!/usr/bin/python3
""" New Function """


def inherits_from(obj, a_class):
    """
    Retuns True if obj is an instance of a\
    class that inherited from the specified class
    Else returns False
    """
    return bool(issubclass(type(obj), a_class) and type(obj) != a_class)
