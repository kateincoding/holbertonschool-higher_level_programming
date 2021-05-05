#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # give the format of a list[2]
    # tuple_a
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
        tuple_a = (0, 0)
    # tuple_b
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        tuple_b = (0, 0)
    # add operation
    tuple_sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (tuple_sum)
