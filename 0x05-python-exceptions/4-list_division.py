#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            div = int(my_list_1[i]) / int(my_list_2[i])
        except(TypeError, ValueError):
            print("wrong type")
            div = 0
            continue
        except(ZeroDivisionError):
            print("division by 0")
            div = 0
            continue
        except(IndexError):
            print("out of range")
            div = 0
            continue
        finally:
            result.append(div)
            pass

    return (result)
