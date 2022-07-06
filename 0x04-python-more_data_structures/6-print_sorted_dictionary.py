#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lk = list(a_dictionary.keys())
    lk.sort()

    for x in lk:
        print("{}: {}".format(x, a_dictionary.get(x)))
