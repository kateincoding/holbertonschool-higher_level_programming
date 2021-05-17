#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return (0)
    try:
        for idx in range(x):
            print(my_list[idx], end="")
    except:
        # case when range(x) > len, the last idx = 1 more
        idx = idx - 1
    finally:
        print()
        return(idx + 1)
