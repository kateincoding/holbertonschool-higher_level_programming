#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """Constructor of the empty class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property for private instance attribute: width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property for private instance attribute: height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method to calculate the area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Method to calculate the perimeter of Rectangle"""
        if self.width <= 0 or self.height <= 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Print a Rectangle to stdout"""
        result = ""
        symbol = str(self.print_symbol)
        if self.width <= 0 or self.height <= 0:
            return result
        else:
            for j in range(self.height):
                for i in range(self.width):
                    result += symbol
                if (j != (self.height - 1)):
                    result = result + "\n"
        return result

    def __repr__(self):
        """Method that return an Unambigous representation of str"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method that executes when object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            rect_2
