#!/usr/bin/python3
"""Class BaseGeometry and Class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Constructor of the Class Rectable"""

    def __init__(self, width, height):
        """Initialization of width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
