#!/usr/bin/python3
"""a class BaseGeometry displaying various errors"""


class BaseGeometry:
    """hasn't been implemented"""
    def area(self):
        """this area raises and exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an int papameter

        Args:
            name (str): name of the parameter
            value (int): validated parmeter
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
