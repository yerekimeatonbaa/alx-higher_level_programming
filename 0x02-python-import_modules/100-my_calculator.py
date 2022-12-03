#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

arlen = len(argv) - 1

if __name__ == "__main__":

    if arlen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

    elif argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

    elif argv[2] == '*' or argv[2] == 'x':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

    elif argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
