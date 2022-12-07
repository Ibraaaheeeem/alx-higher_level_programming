#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    for s in set_1:
        if s not in set_2:
             diff.add(s)
    for s in set_2:
        if s not in set_1:
             diff.add(s)
    return diff
