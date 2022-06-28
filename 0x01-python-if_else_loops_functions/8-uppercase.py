#!/usr/bin/python3
def uppercase(str):
    juu = 0
    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            juu = 32
        else:
            juu = 0
            print("{:c}".format(ord(x) - juu), end="")
    print()
