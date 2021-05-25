#!/usr/bin/python3
def magic_string(result=[]):
    result.append(" Holberton")
    s = ", "
    return s.join(result)

for i in range(10):
    print(magic_string())
