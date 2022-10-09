#!/usr/bin/python3
"""
Print the State obj with 'name' passed as arg from database using sqlalchemy
Script should take 4 args: username, pw, database name, and state name
Must use SQLAlchemy
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

    res = session.query(State.id).filter(State.name == sys.argv[4])

    if (res.first() is None):
        print("Not found")
    else:
        print(res[0][0])
