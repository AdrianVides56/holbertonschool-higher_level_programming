#!/usr/bin/python3
""" Importing """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """
    script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
    safe from MySQL injections!
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY id ASC", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
