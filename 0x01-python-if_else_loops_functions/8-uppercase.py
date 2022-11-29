#!/usr/bin/python3
def uppercase(str):
    upperStr = ""
    for c in str:
        if ord(c) >= 97 or ord(c) <= 122:
            upperStr += chr(ord(c)-32)
        else:
            upperStr += c
    print("{:s}".format(upperStr))
