#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    d = 0

    for ind in range(0, x):
        try:
            print(f"{my_list[ind]}", end="")
            d += 1

        except (TypeError, ValueError, IndexError)
            break

        print()
        return (d)
