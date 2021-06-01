#!/usr/bin/python3
"""Class that inherits from type list"""


class MyList(list):
    """Constructor of Class MyList inherited"""

    def print_sorted(self):
        """prints the sorted"""
        print(sorted(self))
