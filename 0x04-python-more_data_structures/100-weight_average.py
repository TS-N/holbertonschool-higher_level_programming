#!/usr/bin/python3
def weight_average(my_list=[]):
    s = 0
    d = 0
    for tup in my_list:
        s += tup[0] * tup[1]
        d += tup[1]
    return s/d if d else 0
