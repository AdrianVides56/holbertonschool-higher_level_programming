#!/usr/bin/python3
""" Initializes module """


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    for JSON serialization of an object:
    obj is an instance of a class. And al its attirbutes are serializable
    """
    return obj.__dict__
