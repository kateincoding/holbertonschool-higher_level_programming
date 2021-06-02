#!/usr/bin/python3
"""methods module"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from the
    specified class ; otherwise False."""
    if a_class == type(obj):
        return False
    return isinstance(obj, a_class)
