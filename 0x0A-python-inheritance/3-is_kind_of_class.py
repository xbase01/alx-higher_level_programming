#!/usr/bin/python3

"""
    0x0A. Python - Inheritance, Task 3
"""

def is_kind_of_class(obj, a_class):
    """check if an object is an instance of a class,
       or an instance of a class that inherited from
       the specified class
    """
    return isinstance(obj, a_class)
