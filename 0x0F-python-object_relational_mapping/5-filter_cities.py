#!/usr/bin/python3
"""
This script takes the name of a state as an argument
and retrieves a list of all cities within that state
from the database 'hbtn_0e_4_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd-
