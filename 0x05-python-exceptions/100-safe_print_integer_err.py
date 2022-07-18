#!/usr/bin/python3
def safe_print_integer_err(value):

    import sys

    try:
        print("{:d}".format(value))

    except Exception as exx:
        print("Exception:", exx, file=sys.stderr)

        return False
    else:
        return True
