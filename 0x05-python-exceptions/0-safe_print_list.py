#!/usr/bin/python3
"""
Prints x elements in a list

Args:
my_list (list): the list to print from
x (int): number of elemets to print

Returns:
n (int): the number of elements printed

"""

def safe_print_list(my_list=[], x=0):
    n = 0;
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            n += 1
        except IndexError:
            break
    print("")
    return n
