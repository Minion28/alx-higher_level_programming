#!/usr/bin/python3
"""
List states where name' matches argument from MySQL injection.
Username, password, database name, and state name given as user args
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
    cmd = """SELECT id, name
         FROM states
         WHERE name=%s
         ORDER BY id ASC"""
    c.execute(cmd, (sys.argv[4],))
    allstates = c.fetchall()

    for state in allstates:
        print(state)

    c.close()
    db.close()
