#!/usr/bin/python3
"""
List all cities from db in ascending order
Username, password, and database name given as user args
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
    cmd = """SELECT cities.id, cities.name, states.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         ORDER BY cities.id ASC"""
    c.execute(cmd)
    allcities = c.fetchall()

    for city in allcities:
        print(city)

    c.close()
    db.close()
