#!/usr/bin/python3
"Method Module"


def read_file(filename=""):
    """function that reads a txt function UTF8 and printed"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
