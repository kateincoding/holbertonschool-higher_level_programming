#!/usr/bin/python3
"Method Module"
import json


def load_from_json_file(filename):
    """function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'r') as f:
        return(json.load(f))
