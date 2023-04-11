#!/usr/bin/python3

"""
    module lookup contains a method that returns attributes and methods of an object
"""

def lookup(obj):
    """ returns list of attributes and methods of an object"""
    return dir(obj)
