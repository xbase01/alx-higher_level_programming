#!/usr/bin/python3
import sys

args = sys.argv[1:]
total_sum = 0
for arg in args:
    total_sum += int(arg)

print(total_sum)
