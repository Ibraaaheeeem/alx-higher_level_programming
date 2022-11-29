#!/usr/bin/python3
def print_last_digit(number):
    lastN = 0
    if number < 0:
        lastN = ((number * -1)) % 10
    else:
        lastN = number % 10
    print("{:d}".format(lastN), end="")
    return lastN
