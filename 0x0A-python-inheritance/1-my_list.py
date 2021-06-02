#!/usr/bin/python3
"""Class definition"""


class MyList(list):
    """Class MyList inherited"""

    def print_sorted(self):
        """prints the sorted"""
        print(sorted(self))
