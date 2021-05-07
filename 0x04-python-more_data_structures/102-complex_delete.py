#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for x, y in zip(list(a_dictionary.keys()), list(a_dictionary.values())):
        if y == value:
            del a_dictionary[x]
    return a_dictionary
