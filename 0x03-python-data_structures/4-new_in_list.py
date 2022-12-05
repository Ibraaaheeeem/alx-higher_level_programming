#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    this_list = my_list
    if idx < 0 or idx > len(this_list) - 1:
        return this_list
    else:
        this_list[idx] = element
        return this_list
