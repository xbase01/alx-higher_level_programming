#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    errormsg1 = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    errormsg2 = "Unknown operator. Available operators: +, -, * and /"
    if len(argv) != 4:
        print("{}".format(errormsg1))
        exit(1)
    num1 = int(argv[1])
    num2 = int(argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    elif argv[2] == '/':
        print("{} / {} = {}".format(num1, num2, div(num1, num2)))
    else:
        print("{}".format(errormsg2))
        exit(1)
