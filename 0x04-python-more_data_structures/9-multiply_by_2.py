#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = a_dictionary.copy()
    lk = list(nd.keys())

    for x in lk:
        nd[x] *= 2

    return (nd)
