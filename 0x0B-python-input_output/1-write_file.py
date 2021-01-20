#!/usr/bin/python3
""" Intialize module """


def write_file(filename="", text=""):
    """
    Writes text into filename
    Return: Number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(text)
    return len(text)
