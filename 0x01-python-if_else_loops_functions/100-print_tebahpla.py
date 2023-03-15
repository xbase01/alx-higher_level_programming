#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        letter = chr(i).lower()
    else:
        letter = chr(i).upper()
    print("{:s}".format(letter), end="")
