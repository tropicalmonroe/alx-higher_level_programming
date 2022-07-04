#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checkdiv = []

    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            checkdiv.append(True)
        else:
            checkdiv.append(False)

    return (checkdiv)
