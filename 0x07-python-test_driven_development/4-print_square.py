#!/usr/bin/python3
"""
This is "4-print_square.py" module
this module contains print_square function that
prints a square of ####
"""


def print_square(size):
    """
    Prints a square using the '#' character
    Arguments:
        - size: length of the square
        it must be a interger otherwise a TypeError will be raised
        if size is less than 0, a ValueError will be raise
        if size is a float and is less than 0, raise a TypeError
        the last validition is included in the first so it is not
        necessary to include in the code
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is int:
        for i in range(size):
            print('#' * size)
