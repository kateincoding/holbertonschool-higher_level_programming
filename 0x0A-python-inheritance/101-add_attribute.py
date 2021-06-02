#!/usr/bin/python3


def add_attribute(object, key, value):
    """Method to add new attribute if it is possible=type(dict)"""

    if hasattr(object, "__dict__") == False:
        raise TypeError("can't add new attribute")
    setattr(object, key, value)

class MyClass():
    pass
