#!/usr/bin/python3
"Method Module"


class Student:
    """My class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            k = {}
            for a in attrs:
                if a in self.__dict__:
                    k[a] = self.__dict__[a]
            return k
        return self.__dict__
