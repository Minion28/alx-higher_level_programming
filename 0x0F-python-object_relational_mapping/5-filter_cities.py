#!/usr/bin/python3
"""
List all cities in ascending order from db by given state
Username, password, database name, and state name given as user args
Use execute() once
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
    cmd = """SELECT cities.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         WHERE states.name=%s
         ORDER BY cities.id ASC"""
    c.execute(cmd, (sys.argv[4],))
    allcities = c.fetchall()

    print(", ".join([city[0] for city in allcities]))

    c.close()
    db.close()
