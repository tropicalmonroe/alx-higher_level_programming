#!/usr/bin/python3
def max_integer(my_list=[]):
    refu = len(my_list)

    if refu == 0:
        return (None)

    mxint = my_list[0]

    for x in range (1, refu):
        if my_list[x] > mxint:
            mxint = my_list[x]

    return (mxint)
