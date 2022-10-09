#!/usr/bin/python3
"""
Start a link class to table in database
"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
