#!/usr/bin/python3
def no_c(my_string):
    tall = len(my_string)

    z = 0

    newstring = my_string[:]

    for x in range(tall):
        if (my_string[x] == 'c' or my_string[x] == 'C'):
            newstring = newstring[:(x - z)] + my_string[(x + 1):]
            z += 1

    return (newstring)
