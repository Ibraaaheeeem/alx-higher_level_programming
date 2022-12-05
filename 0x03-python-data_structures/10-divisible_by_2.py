#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    by2 = []
    for i in range(len(my_list)):
        by2.append(my_list[i] % 2 == 0)
    return by2
