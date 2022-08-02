#!/usr/bin/python3
""" a class BaseGeometry that raises an Exception"""


class BaseGeometry:
    """rep base geomentry"""

    def area(self):
        """raised exception if not implemented"""
        raise Exception("area() is not implemented")
