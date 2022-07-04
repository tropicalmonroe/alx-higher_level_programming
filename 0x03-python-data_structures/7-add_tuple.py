#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenth_a = len(ta)
    lenth_b = len(tb)

    if lenth_a == 0:
        aa = 0
        ab = 0
    elif lenth_a == 1:
        aa = ta[0]
        ab = 0
    else:
        aa = ta[0]
        ab = ta[1]

    if lenth_b == 0:
        bb = 0
        bc = 0
    elif lenth_b == 1:
        bb = tb[0]
        bc = 0
    else:
        bb = tb[0]
        bc = tb[1]

    nt = (aa + bb, ab + ac)

    return (nt)
