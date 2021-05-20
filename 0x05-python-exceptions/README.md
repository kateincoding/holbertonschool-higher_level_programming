# Python - Exceptions

## Lecture Resources

## Learning Objectives

 * Why Python programming is awesome
 * What’s the difference between errors and exceptions
 * What are exceptions and how to use them
 * When do we need to use exceptions
 * How to correctly handle an exception
 * What’s the purpose of catching exceptions
 * How to raise a builtin exception
 * When do we need to implement a clean-up action after an exception

## How to know what kind of errors your code have:

```
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            pass
```

## How to check you disambly Bytecode:
```
        import dis
        dis.dis(magic_calculation)
```

## Functions

##|File|Description
---|---|---
0|[0-safe_print_list.py](./0-safe_print_list.py)|0. Safe list printing
1|[1-safe_print_integer.py](./1-safe_print_integer.py)|1. Safe printing of an integers list
mandatory
2|[2-safe_print_list_integers.py](./2-safe_print_list_integers.py)|2. Print and count integers
