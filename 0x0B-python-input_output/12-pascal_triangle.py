#!/usr/bin/python3
"""Module to create a Pascal triangle"""


def next_list(list=[]):
    """Function to generate the next_list"""

    mask1 = list[:]
    mask2 = list[:]

    del mask1[0]
    mask2.pop()
    len_mask = int(len(mask1) / 2) + (len(mask1) % 2)
    middle_result = [mask1[i] + mask2[i] for i in range(0, len_mask)]
    reverse_result = middle_result[::-1]
    if (len(list) % 2 == 0):
        del reverse_result[0]
    result = [1] + middle_result + reverse_result + [1]
    return result


def pascal_triangle(n):
    """Function to create Pascal_triangle"""

    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    l = []
    l.append([1])
    l.append([1, 1])
    for i in range(2, n):
        l.append(next_list(l[i - 1]))
    return l
