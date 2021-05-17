#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return (0)
    number = 0
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            number = number + 1
        except (ValueError, TypeError):
            pass
    print()
    return(number)
