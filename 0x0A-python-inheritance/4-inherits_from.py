#!/usr/bin/python3
"""a function that returns True or False"""


def inherits_from(obj, a_class):
    """checks if an object is an inherited instance
    Args:
        obj (any): The object t check
        a_class (type): The class to match the type of obj
    Returns:
        If obj is an inherited instance of a_class - True/othrwise false
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
