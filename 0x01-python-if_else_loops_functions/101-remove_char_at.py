#!/usr/bin/python3
def remove_char_at(str, n):
    cpystr = ""
    m = 0
    for at in str:
        if m != n:
            cpystr += at
            m += 1
        else:
            m += 1
            continue
    return cpystr
