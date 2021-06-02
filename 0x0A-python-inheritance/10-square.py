#!/usr/bin/python3
"""Class BaseGeometry and Class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Rectable"""

    def __init__(self, size):
        """Constructor: Initialization of width and height"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method: area calculation"""
        return(super().area())
