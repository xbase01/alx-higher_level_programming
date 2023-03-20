#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tempsum = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            tempsum[i] += tuple_a[i]
        if i < len(tuple_b):
            tempsum[i] += tuple_b[i]
    return tuple(tempsum)
