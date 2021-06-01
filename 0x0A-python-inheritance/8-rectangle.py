#!/usr/bin/python3
"""Class BaseGeometry and Class Rectangle"""


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


class Rectangle(BaseGeometry):
    """Constructor of the Class Rectable"""

    def __init__(self, width, height):
        """Initialization of width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
