#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqint = set(my_list)
    num = 0

    for x in uniqint:
        num += x
    return (num)
