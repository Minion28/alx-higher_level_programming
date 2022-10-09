#!/usr/bin/python3
"""
Print the first 'State' object from database using sqlalchemy
Script should take 3 args: username, pw, and database name
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State.id, State.name).first()
    if (res is None):
        print("Nothing")
    else:
        print("{:d}: {}".format(res[0], res[1]))
