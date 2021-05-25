# 0x08. Python - More Classes and Objects

## Lecture Resources

Read or watch:

* Object Oriented Programming (Read everything until the paragraph“Inheritance” (excluded))
* Object-Oriented Programming (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
* Class and Instance Attributes
* classmethods and staticmethods
* Properties vs. Getters and Setters (Mainly the last part “Public instead of Private Attributes”)
* str vs repr

## Learning Objectives

* Why Python programming is awesome
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* What are the special __str__ and __repr__ methods and how to use them
* What is the difference between __str__ and __repr__
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

## Differente between str and repr

Check if the str of eval(repr) will be the same of str:
,,,
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))

    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
,,,

## Functions

##|File|Description
---|---|---
0|[0-rectangle.py](./0-rectangle.py)|0. create the class of a simple Rectangle
1|[1-rectangle.py](./1-rectangle.py)|1. Real definition of a rectangle
2|[2-rectangle.py](./2-rectangle.py)|2. Area and Perimeter
3|[3-rectangle.py](./3-rectangle.py)|3. String representation
4|[4-rectangle.py](./4-rectangle.py)|4. Eval is magic
5|[5-rectangle.py](./5-rectangle.py)|5. Detect instance deletion
6|[6-rectangle.py](./6-rectangle.py)|6. How many instances
mandatory
7|[7-rectangle.py](./7-rectangle.py)|7. Change representation
mandatory
8|[8-rectangle.py](./8-rectangle.py)|8. Compare rectangles
9|[9-rectangle.py](./9-rectangle.py)|9. A square is a rectangle
10|[Class and instance attributes
](./9-rectangle.py)|Medium Blog
11|[101-nqueens.py](./101-nqueens.py)|11. N queens

## Test Files

##|File|Description
---|---|---
0|[tests/0-main.py](tests/0-main.py)|0. Test for class 0-rectangle.py
1|[tests/1-main.py](tests/1-main.py)|1. Test for class 1-rectangle.py
2|[tests/2-main.py](tests/2-main.py)|2. Test for class 2-rectangle.py
3|[tests/3-main.py](tests/3-main.py)|3. Test for class 3-rectangle.py
4|[tests/4-main.py](tests/4-main.py)|4. Test for class 4-rectangle.py
5|[tests/5-main.py](tests/5-main.py)|5. Test for class 5-rectangle.py
6|[tests/6-main.py](tests/6-main.py)|6. Test for class 6-rectangle.py
7|[tests/7-main.py](tests/7-main.py)|7. Test for class 7-rectangle.py
8|[tests/8-main.py](tests/8-main.py)|8. Test for class 8-rectangle.py
9|[tests/9-main.py](tests/9-main.py)|9. Test for class 9-rectangle.py
