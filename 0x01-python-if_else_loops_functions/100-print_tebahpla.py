#!/usr/bin/python3
for letter in reversed(range(97, 123)):
    print("{:}".format(chr(letter - 32) if letter % 2 != 0
                       else chr(letter)), end="")
