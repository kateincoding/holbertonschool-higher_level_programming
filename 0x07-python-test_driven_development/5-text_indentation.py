#!/usr/bin/python3
"""
This is "text_indentation" module

this module contains text_indentation function,
prints a text with 2 new lines after each of these
characters: '.', '?' and ':'
"""


def text_indentation(text):
    """Return string divided by spaces
    Arguments:
        text (string): string to be formmated

    raises:
        TypeError: if the text called with the program is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    text = text.strip()
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag is 1:
            if i == '.' or i == '?' or i == ':':
                print(i)
                print()
                flag = 0
            else:
                print(i, end='')
