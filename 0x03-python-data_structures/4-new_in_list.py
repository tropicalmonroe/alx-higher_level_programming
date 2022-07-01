#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tall = len(my_list)
    newlist = my_list[:]

    if 0 <= idx < tall:
        newlist[idx] = element

    return (newlist)
