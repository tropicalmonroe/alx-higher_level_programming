#!/usr/bin/python3
if __name__ == "__main__"
import sys
x = len(sys.argv) - 1

if x == 0:
    print("{} arguments".format(x))
elif x == 1:
    print("{} arguments".format(x))
else:
    print("{} arguments".format(x))

    if x >= 1:
        x = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
