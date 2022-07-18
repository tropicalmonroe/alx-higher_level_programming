#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    d = 0

    for ind in (0, x):
        try:
            print("{:d}".format(my_list=[ind]), end="")
            d += 1

        except (ValueError, TypeError):
            continue

        print()
        return (d)
