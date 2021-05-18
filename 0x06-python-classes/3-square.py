#!/usr/bin/python3
class Square:
    """ Definition of Class Square """
    def __init__(self, size=0):
        """ Size is a private attribute :
            - size must be an integer, otherwise raise a TypeError exception
              with the message size must be an integer
            - if size is less than 0, raise a ValueError exception with the
              message size must be >= 0 """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Public instance method:
            * Return: the current square area """
        return(self.__size * self.__size)
