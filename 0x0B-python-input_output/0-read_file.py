#!/usr/bin/python3
"""Defines file reading func"""


def read_file(filename=""):
    """stdout a UTF8 encode content"""
    with open(filename, encoding="utf-8") as x:
        print(x.read(), end="")
