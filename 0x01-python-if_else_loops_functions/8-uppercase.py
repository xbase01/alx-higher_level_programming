#!/usr/bin/python3
def uppercase(s):
    for c in s:
        ascii_code = ord(c)
        if 97 <= ascii_code <= 122:
            uppercase_ascii_code = ascii_code - 32
            print("{:c}".format(uppercase_ascii_code), end="")
        else:
            print("{:c}".format(ascii_code), end="")
    print()
