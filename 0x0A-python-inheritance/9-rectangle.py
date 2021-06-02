#!/usr/bin/python3
"""Class definition"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectable"""

    def __init__(self, width, height):
        """Constructor of Initialization of width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method: area calculation"""
        return(self.__width * self.__height)

    def __str__(self):
        """Builtin str that will executes when print method is used"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
