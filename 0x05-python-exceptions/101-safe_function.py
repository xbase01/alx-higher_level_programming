#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as exc:
        print("Exception: {}".format(exc), file=sys.stderr)
        result = None
    return result
