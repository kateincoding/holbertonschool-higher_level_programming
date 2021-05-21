#!/usr/bin/python3
def transpose(m_b):
    """transpose a matrix in order to make mul easier"""
    new_matrix = []
    for column in m_b[0]:
        new_matrix.append([])
    for row in m_b:
        for index, elm in enumerate(row):
            new_matrix[index].append(elm)
    return new_matrix

def product_maker(row_a, row_b):
    """multipies elements"""
    sum = 0
    for index, elm in enumerate(row_a):
        sum += elm * row_b[index]
    return sum

def multiplier(m_a, m_b):
    """Multiply matrix"""
    tr_b = transpose(m_b)
    new_matrix = []
    for row in m_a:
        new_matrix.append([])
    
    f_product = 0
    for index_m_a, row_a in enumerate(m_a):
        for index_m_b, row_b in enumerate(tr_b):
            f_product = product_maker(row_a, row_b)
            new_matrix[index_m_a].append(f_product)
    return new_matrix


def matrix_mul(m_a, m_b):
    """ Error Messages"""

    a_list_error = "m_a must be a list"
    b_list_error = "m_b must be a list"
    a_list_of_list_error = "m_a must be a list of lists"
    b_list_of_list_error = "m_b must be a list of lists"
    a_empty_error = "m_a can't be empty"
    b_empty_error = "m_b can't be empty"
    a_wrong_element = "m_a should contain only integers or floats"
    b_wrong_element = "m_b should contain only integers or floats"
    a_size_error = "each row of m_a must be of the same size"
    b_size_error = "each row of m_b must be of the same size"
    cannot_mul = "m_a and m_b can't be multiplied"

    if type(m_a) is not list:
        raise TypeError(a_list_error)
    if type(m_b) is not list:
        raise TypeError(b_list_error)
    
    if m_a == []:
        raise ValueError(a_empty_error)
    if m_b == []:
        raise ValueError(b_empty_error)
    
    size_a = len(m_a[0])
    size_b = len(m_b[0])
    

    for row in m_a:
        if row == []:
            raise ValueError(b_empty_error)
        if type(row) is not list:
            raise TypeError(a_list_of_list_error)
        if len(row) != size_a:
            raise TypeError(a_size_error)
        for elm in row:
            if type(elm) is not int and type(elm) is not float:
                raise TypeError(a_wrong_element)

    for row in m_b:
        if row == []:
            raise ValueError(b_empty_error)
        if type(row) is not list:
            raise TypeError(b_list_of_list_error)
        if len(row) != size_b:
            raise TypeError(b_size_error)
        for elm in row:
            if type(elm) is not int and type(elm) is not float:
                raise TypeError(b_wrong_element)
    if size_a != len(m_b):
        raise ValueError(cannot_mul)
    

    return multiplier(m_a, m_b)
