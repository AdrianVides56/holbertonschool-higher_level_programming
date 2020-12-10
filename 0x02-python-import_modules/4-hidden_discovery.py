#!/usr/bin/python3
if __name__ == "__main__":
    import sys, hidden_4

for a in dir(hidden_4):
    if a[0:2] == "__":
        continue
    print(a)
