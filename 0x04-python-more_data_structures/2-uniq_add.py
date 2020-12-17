#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    addit = 0
    for a in new:
        addit += int(a)
    return addit
