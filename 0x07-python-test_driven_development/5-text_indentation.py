#!/usr/bin/python3
"""
Creating a new function:

text_indentation
"""


def text_indentation(text):
    """
    text_indentation - prints a text with 2 new lines
    after each of these characters: '., ?, :' (dot, question mark, colon)
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    space = 0
    for a in text:
        if space == 0:
            if a == ' ':
                continue
            else:
                space = 1
        if a == '.' or a == '?' or a == ':':
            print(a)
            print()
            space = 0
        else:
            print(a, end="")
