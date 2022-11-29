#!/usr/bin/python3
def uppercase(str):
    upperStr = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 or ord(str[i]) <= 122:
            upperStr += str(chr(i-32))
        else:
            upperStr += str(chr(i))
    print("{:s}".format(upperStr))
