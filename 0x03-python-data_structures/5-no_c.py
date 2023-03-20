#!/usr/bin/python3

def no_c(my_string):
    lstr = list(my_string)
    new_str = ''
    for i in range(len(lstr)):
        if lstr[i].upper() == 'C':
            lstr[i] = ''
        new_str += lstr[i]
    return new_str
