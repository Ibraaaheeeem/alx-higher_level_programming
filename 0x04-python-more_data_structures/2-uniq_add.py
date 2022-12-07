#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniqs = []
    for item in my_list:
        if item not in uniqs:
            sum += item
            uniqs.append(item)
    return sum
