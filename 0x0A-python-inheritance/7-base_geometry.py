#!/usr/bin/python3
"""Empty Class BaseGeometry"""


class BaseGeometry():
    """Constructor of the class"""

    def area(self):
        """Function to calculate area that is not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validate if is an integer
        name is alwas a string"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
