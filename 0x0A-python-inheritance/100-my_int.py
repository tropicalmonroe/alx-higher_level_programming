#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """exchnage ops == and !="""

    def __eq__(self, value):
        """override"""
        return self.real != value

    def __ne__(self, value):
        """Override"""
        return self.real == value
