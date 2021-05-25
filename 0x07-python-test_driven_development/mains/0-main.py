#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as ex: 
    template = "An exception of type {0} occurred. Arguments:\n{1!r}" 
    message = template.format(type(ex).name, ex.args)
    print(message) 
    pass
