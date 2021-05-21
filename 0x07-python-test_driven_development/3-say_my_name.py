#!/usr/bin/python3
"""
This is "3-say_my_name.py" module
this module contains say_my_name function that
prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """Return the print of the full name
    Arguments:
        first_name (string): first string to print
        last_name (string): second string to print
    Return:
        print full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
