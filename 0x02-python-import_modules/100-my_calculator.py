#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    argc = len(argv)
    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    i = 0
    a = int(argv[1])
    b = int(argv[3])
    operators = [('+', add), ('-', sub), ('*', mul), ('/', div)]
    while (i <= 3):
        op = operators[i][0]
        if argv[2] == op:
            print("{} {} {} = {}".format(a, argv[2], b, operators[i][1](a, b)))
            break
        i += 1
        if (i == 4):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
