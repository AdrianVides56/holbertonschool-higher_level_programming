#!/usr/bin/python3
if __name__ == "__main__":
    import sys

num = 0

if len(sys.argv) == 2:
    print(int(sys.argv[1]))
else:
    for a in range(1, len(sys.argv)):
        num = num + int(sys.argv[a])
    print(num)
