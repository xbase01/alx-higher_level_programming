#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for element in my_list:
        try:
            if isinstance(element, int):
                print("{:d}".format(element))
                i += 1
        except:
            pass
        if i == x:
            break
    return i
