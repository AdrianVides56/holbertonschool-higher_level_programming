#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = 0
        the_key = ""
        for a in a_dictionary:
            if a_dictionary[a] > best:
                best = a_dictionary[a]
                the_key = a
        return the_key
    return None
