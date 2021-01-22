#!/usr/bin/python3
""" Initializes module and import """
import json


def load_from_json_file(filename):
    """ Creates an Object from filename (json file) """
    with open(filename) as my_file:
        return json.load(my_file)
