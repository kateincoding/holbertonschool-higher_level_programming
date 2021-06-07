#!/usr/bin/python3
"""Module for the class Base"""
import json
import csv
import turtle


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON string representation
        of list_dictionaries
        - list_dictionary: must be a list of dictionary
        - Return: string of dictionary in json format"""
        if list_dictionaries is None:
            return "[]"
        else:
            string = json.dumps(list_dictionaries)
            return string

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string
        representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        result = []
        if list_objs:
            for objs in list_objs:
                dictionary = objs.to_dictionary()
                result.append(dictionary)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON
        string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, encoding="utf-8") as file:
                obj_list = cls.from_json_string(file.read())
                for dictionary in obj_list:
                    result.append(cls.create(**dictionary))
                return result
        except:
            return result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method to serialize in csv
        input: object (you can have the information with dict)
        result: [[4, 5, 0, 0], [5, 7, 9, 1]]"""
        list_rectangle = ["id", "width", "height", "x", "y"]
        list_square = ["id", "size", "x", "y"]
        filename = cls.__name__ + ".csv"
        result = []

        if list_objs:
            for objs in list_objs:
                # First recollect the info of the object with a dict
                dictionary = objs.to_dictionary()
                middle_result = []
                # Second obtein the values in a ordered class list
                if cls.__name__ == "Rectangle":
                    for item in list_rectangle:
                        middle_result.append(dictionary[item])
                if cls.__name__ == "Square":
                    for item in list_square:
                        middle_result.append(dictionary[item])
                # append the list to result list
                result.append(middle_result)
        with open(filename, "w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(result)

    @classmethod
    def load_from_file_csv(cls):
        """Method to deserialize in csv
        input: ['1', '10', '7', '2', '8']
        first: you need to create a dictionary of the instance
        {'width': '10', 'height': '7', 'id': '1', 'x': '2', 'y': '8'}
        second: you need to create() an object from the dict
        Return: [140462163445632] [Square] (5) 0/0 - 5"""
        list_rectangle = ["id", "width", "height", "x", "y"]
        list_square = ["id", "size", "x", "y"]
        filename = cls.__name__ + ".csv"
        dictionary = []
        result = []

        try:
            with open(filename, encoding="utf-8") as file:
                obj_list = csv.reader(file)
                # read obj_list <_csv.reader object at 0x7fbfe5614b38>
                if cls.__name__ == "Rectangle":
                    for list in obj_list:
                        # create dictionary
                        dict = {}
                        for key, value in zip(list_rectangle, list):
                            dict[key] = int(value)
                        # create an object and append to a list
                        result.append(cls.create(**dict))
                if cls.__name__ == "Square":
                    for list in obj_list:
                        # create dictionary
                        dict = {}
                        for key, value in zip(list_square, list):
                            dict[key] = int(value)
                        # create an object and append to a list
                        result.append(cls.create(**dict))
                return result
        except:
            return result

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Method that opens a window and draws
        all the Rectangles and Squares"""

        art = turtle.Turtle()

        def set_position(x, y):
            art.penup()
            art.goto(x, y)
            art.pendown()

        def beauty_rectangle(width, height, art):
            art.begin_fill()
            for i in range(2):
                art.forward(width)
                art.right(90)
                art.forward(height)
                art.right(90)
            art.end_fill()

        for rectangle in list_rectangles:
            art.color("#800080")
            set_position(rectangle.x, rectangle.y)
            beauty_rectangle(rectangle.width, rectangle.height, art)
            set_position(-1 * rectangle.x, -1 * rectangle.y,)

        for square in list_squares:
            art.color("#40E0D0")
            set_position(square.x, square.y)
            beauty_rectangle(square.size, square.size, art)
            set_position(-1 * square.x, -1 * square.y)

        turtle.done()
