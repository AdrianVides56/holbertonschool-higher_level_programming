#!/usr/bin/python3
""" module 6-peak """


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers """
    if len(list_of_integers) < 1:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
