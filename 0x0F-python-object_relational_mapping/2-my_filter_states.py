#!/usr/bin/python3
"""
This script accepts an argument and retrieves
all records from the hbtn_0e_0_usa database
where the name field matches the provided argument.
The matching values are then displayed.
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                         WHERE name LIKE BINARY '{}' \
                         ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
