#!/usr/bin/python3
"""function that returns True or false otherwise"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance
    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of obj
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
