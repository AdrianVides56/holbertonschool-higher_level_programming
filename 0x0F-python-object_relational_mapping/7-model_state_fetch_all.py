#!/usr/bin/python3
""" Importing """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ list all State objects from db hbtn_0e_6_usa"""
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State).order_by(State.id).all():
        print('{}: {}'.format(row.id, row.name))

    session.close()
