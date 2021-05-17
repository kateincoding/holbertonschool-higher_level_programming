#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list or x == 0:
        return (0)
    number = 0
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            number = number + 1
        # except Exception as ex:
        #    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        #    message = template.format(type(ex).__name__, ex.args)
        #    print(message)
        #    pass
        except (ValueError, TypeError):
            pass
    print()
    return(number)
