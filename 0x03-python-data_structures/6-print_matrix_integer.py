#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix[0:]:
        for j in i[0:]:
            print(" {:d}".format(j), end="")
        print()
