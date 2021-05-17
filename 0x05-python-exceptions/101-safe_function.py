#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        result = None
    finally:
        return (result)
