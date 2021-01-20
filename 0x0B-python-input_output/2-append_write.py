#!/usr/bin/python3
""" Intializing module"""


def append_write(filename="", text=""):
    """
    Appends text into filename
    Return: number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as myFile:
        myFile.write(text)
    return len(text)
