#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if (j >= ord('a') and j <= ord('z')):
            j -= ord('a') - ord('A')
        print("{:c}".format(j), end="")
    print()
