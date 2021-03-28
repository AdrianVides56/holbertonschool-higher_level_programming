#!/usr/bin/python3
""" Importing """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """ lists all states with a name starting with N """
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         password=argv[2],
                         database=argv[3],
                         port=3306)

    """ Creating cursor """
    cur = db.cursor()

    """ Instruction to the database """
    cur.execute("SELECT * FROM states WHERE\
    name REGEXP '^N.+' ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)

    """ Clean up """
    cur.close()
    db.close()
