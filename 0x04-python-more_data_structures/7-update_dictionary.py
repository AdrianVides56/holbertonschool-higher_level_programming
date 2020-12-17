#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for a in a_dictionary:
        if a == key:
            a_dictionary[a] = value
    a_dictionary[key] = value
    return a_dictionary
