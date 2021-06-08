#!/usr/bin/python3
"""Module for the class Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Base inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """property of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size but unsing the attribute of Rectangle:
        - first width because we want the error validation of its"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """refresh the values of square attributes"""
        args_list = ["id", "width", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def __str__(self):
        """overriding to return [Square] + more information"""
        string = "[Square] ({:d}) {:d}/{:d} - {:d}"
        string = string.format(self.id, self.x, self.y, self.width)
        return string

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle"""
        key_list = ["id", "size", "x", "y"]
        value_list = [self.id, self.width, self.x, self.y]
        return dict(zip(key_list, value_list))
