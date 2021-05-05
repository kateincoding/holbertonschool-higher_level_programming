#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix[0:]:
        spc = ""
        for j in i[0:]:
            print("{:s}{:d}".format(spc, j), end="")
            spc = " "
        print()
