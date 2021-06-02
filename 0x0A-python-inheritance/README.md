# 0x0A. Python - Inheritance

![Inheritance types](https://bytesofgigabytes.com/IMAGES/java/Inheritance/typesofInheritance.png)

## Lecture Resources

Read or watch:

* [Inheritance](https://docs.python.org/3.4/tutorial/classes.html#inheritance)
* [Multiple inheritance](https://docs.python.org/3.4/tutorial/classes.html#multiple-inheritance)
* [Inheritance in Python](https://hub.packtpub.com/inheritance-python/)
* [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk&ab_channel=DerekBanas)

## Learning Objectives

* Why Python programming is awesome
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use isinstance, issubclass, type and super built-in functions

## Differente between type() and isinstance()

Check if the str of eval(repr) will be the same of str:
,,,

    >>> isinstance(True, int)
    Truee

    >>> type(True) == int
    False

    >>> type(True)
    <class 'bool'>
,,,

## Functions

##|File|Description
---|---|---
0|[0-lookup.py](./0-lookup.py)|Write a function that returns the list of available attributes and methods of an object:
1|[1-my_list.py](./1-my_list.py)|Write a class MyList that inherits from list
2|[2-is_same_class.py](./2-is_same_class.py)|Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False
3|[3-is_kind_of_class.py](./3-is_kind_of_class.py)|Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
4|[4-inherits_from.py](./4-inherits_from.py)|Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
5|[5-base_geometry.py](./5-base_geometry.py)|Write an empty class BaseGeometry
6|[6-base_geometry.py](./6-base_geometry.py)|Write a class BaseGeometry (based on 5-base_geometry.py) with a Public instance method: def area(self): that raises an Exception with the message area() is not implemented
7|[7-base_geometry.py](./7-base_geometry.py)|Write a class BaseGeometry (based on 6-base_geometry.py). Public instance method: def integer_validator(self, name, value): that validates value:if value is not an integer: raise a TypeError exception, with the message <name> must be an integer. Otherwise: if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
8|[8-rectangle.py](./8-rectangle.py)|Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).Instantiation with width and height: def __init__(self, width, height):width and height must be private. No getter or setter width and height must be positive integers, validated by integer_validator
9|[9-rectangle.py](./9-rectangle.py)|Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)Instantiation with width and height: def __init__(self, width, height):: width and height must be private. No getter or setter ; width and height must be positive integers validated by integer_validator the area() method must be implemented ; print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
10|[10-square.py](./10-square.py)|Write a class Square that inherits from Rectangle (9-rectangle.py): Instantiation with size: def __init__(self, size):: size must be private. No getter or setter | size must be a positive integer, validated by integer_validator | the area() method must be implemented
11|[11-square.py](./11-square.py)|Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).Instantiation with size: def __init__(self, size):: size must be private. No getter or setter | size must be a positive integer, validated by integer_validator | the area() method must be implemented | print() should print, and str() should return, the square description: [Square] <width>/<height>

## Test Files

##|File|Description
---|---|---
0|[tests/1-my_list.txt](tests/1-my_list.txt)|Test for class my-list
1|[tests/7-base_geometry.txt](tests/7-base_geometry.txt)|Test for class base_geometry

