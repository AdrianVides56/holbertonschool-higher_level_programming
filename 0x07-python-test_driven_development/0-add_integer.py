#!/usr/bin/python3
"""
Crating a new function:

add_integer
"""


def add_integer(a, b=98):
    """add_integer - adds two numbers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        b = int(b)

    return a + b
