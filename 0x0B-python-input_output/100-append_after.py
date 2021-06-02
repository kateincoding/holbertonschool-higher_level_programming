#!/usr/bin/python3
"""Module to create a Pascal triangle"""


def append_after(filename="", search_string="", new_string=""):
    """append after a line"""
    with open(filename, "r") as f:
        list_lines = f.readlines()
        result = []
        for line in list_lines:
            result.append(line)
            if search_string in line:
                result.append(new_string)
        f = open(filename, "w")
        f.writelines(result)
