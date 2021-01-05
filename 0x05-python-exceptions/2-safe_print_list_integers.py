#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            idx += 1
        except (TypeError, ValueError):
            pass
    print()
    return idx