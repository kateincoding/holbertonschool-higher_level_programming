#!/usr/bin/python3
for c in range(97, 123):
    if c != 101 and c != 113:  # not e neither q
        print("{:c}".format(c), end="")
