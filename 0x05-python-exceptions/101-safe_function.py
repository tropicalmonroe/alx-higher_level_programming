#!/usr/bin/python3
def safe_function(fct, *args):

    import sys

    try:
        return fct(*args)

    except Exception as exx:
        print("Exception:", exx, file=sys.stderr)

        return None
