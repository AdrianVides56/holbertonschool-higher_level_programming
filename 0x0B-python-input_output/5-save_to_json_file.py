#!/usr/bin/python3
""" Initializes module and import json"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes my_obj into filename using JSON representation
    """
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
