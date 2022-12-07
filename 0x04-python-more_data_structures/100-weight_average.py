#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_of_weighted_score =  sum([x[0] * x[1] for x in my_list])
    sum_of_weights = (sum([x[1] for x in my_list]) or 1)
    return sum_of_weighted_score / sum_of_weights
