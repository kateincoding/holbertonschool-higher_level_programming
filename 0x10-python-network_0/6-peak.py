#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find a peak in an unsurted list"""

    if not list_of_integers:
        return None

    return max(list_of_integers)
