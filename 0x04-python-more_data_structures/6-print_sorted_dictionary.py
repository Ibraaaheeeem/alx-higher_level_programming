#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items(), key = lambda x: x[0])
    return dict(sorted_dict)
