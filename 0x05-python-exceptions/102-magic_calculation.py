#!/usr/bin/python3
def magic_calculation(a, b):

    x = 0

    for ind in range(1, 3):
        try:
            if ind > a:
                raise Exception('Too far')

            else:
                x += (a ** b) / ind
        except Exception:
            x = a + b
            break

        return x
