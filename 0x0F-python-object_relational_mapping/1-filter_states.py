#!/usr/bin/python3
"""
List all states with a name starting with uppercase N
Username, password, and database names are given as user args
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    c = db.cursor()
    cmd = """
    SELECT id, name
             FROM states
             WHERE name LIKE BINARY 'N%'
             ORDER BY id ASC;
             """
    c.execute(cmd)
    allstates = c.fetchall()

    for state in allstates:
        print(state)

    c.close()
    db.close()
