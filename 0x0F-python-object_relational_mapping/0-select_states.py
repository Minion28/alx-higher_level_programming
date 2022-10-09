#!/usr/bin/python3
"""
list all states from hbtn_0e_0_usa database
username, password, and database be given as user args
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user = sys.argv[1],
            password = sys.argv[2],
            db = sys.argv[3],
            host = 'localhost',
            port = 3306)
    c = db.cursor()
    c.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    states = c.fetchall()
    
    for state in states:
        print (state)

    c.close()
    db.close()
