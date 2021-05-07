#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    # pow_column = lambda column: column**2
    # pow_row = lambda row: list(map(pow_column, row))
    return (list(map(lambda row: list(map(lambda col: col**2, row)), matrix)))
