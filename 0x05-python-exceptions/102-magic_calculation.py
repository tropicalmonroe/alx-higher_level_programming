#!/usr/bin/python3
def magic_calculation(a, b):

    x = 0

    for count in range(1, 3):
        try:
            if count > a:
                raise Exception('Too far')

            else:
                x += (a ** b) / count
        except Exception:
            x = a + b
            break

        return x
