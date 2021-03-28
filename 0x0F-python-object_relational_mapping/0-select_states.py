#!/usr/bin/python3
"""" Importing """
import MySQLdb
from sys import argv

if __name__ == "__main__":
  """ lists states from hbtn_0a_usa db """
  db = MySQLdb.connect(host='localhost',
                       port=3306,
                       user=argv[1],
                       password=argv[2],
                       db=argv[3])

  """ Crating Cursor for database"""
  cur = db.cursor()

  """ Instruction to the database """
  cur.execute("SELECT * FROM states ORDER BY id ASC")

  for row in cur.fetchall(): #printing
    print(row)

  """ Clean Up """
  cur.close()
  db.close()
