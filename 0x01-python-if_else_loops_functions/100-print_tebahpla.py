#!/usr/bin/python3
for words in reversed(range(97, 123)):
    print("{:c}".format(words if (words % 2 == 0) else (words - 32)), end='')
