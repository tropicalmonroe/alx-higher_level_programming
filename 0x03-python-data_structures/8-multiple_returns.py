#!/usr/bin/python3
def multiple_returns(sentence):
    ls = len(sentence)

    if (ls == 0):
        nt = (ls, None)
    else:
        nt = (ls, sentence[0])

    return (nt)
