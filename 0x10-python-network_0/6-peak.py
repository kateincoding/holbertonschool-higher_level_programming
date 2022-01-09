#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find a peak in an unsurted list"""

    if not list_of_integers:
        return None

    Min = 0
    Max = len(list_of_integers) - 1

    pivot = list_of_integers[Max]
    for x in list_of_integers:
        if x > pivot:
            pivot = x

    return pivot
