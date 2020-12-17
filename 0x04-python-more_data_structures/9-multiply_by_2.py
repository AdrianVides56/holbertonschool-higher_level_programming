#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for a in a_dictionary:
        new[a] = int(a_dictionary[a]) * 2
    return new
