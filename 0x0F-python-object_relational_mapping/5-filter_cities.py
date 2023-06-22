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
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM cities INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id""")
    print(", ".join([city[2] for city in cur.fetchall()
                     if city[4] == argv[4]]))
