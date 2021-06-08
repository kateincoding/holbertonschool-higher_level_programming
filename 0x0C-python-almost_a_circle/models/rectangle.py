#!/usr/bin/python3
"""Module for the class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method to calculate the area of rectangle"""
        return(self.width * self.height)

    def display(self):
        """Method to display a square of #"""
        for y in range(0, self.y):
            print()
        for j in range(0, self.height):
            for x in range(0, self.x):
                print(" ", end="")
            for i in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding to returns [Rectangle] + information"""
        string = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        string = string.format(self.id, self.x, self.y,
                               self.width, self.height)
        return string

    def update(self, *args, **kwargs):
        """Method that assigns update attributes"""
        args_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle"""
        key_list = ["id", "width", "height", "x", "y"]
        value_list = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(key_list, value_list))
