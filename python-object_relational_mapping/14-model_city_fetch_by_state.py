#!/usr/bin/python3
"""Print all City objects with their State name sorted by cities.id."""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = (
        session.query(State, City)
        .filter(City.state_id == State.id)
        .order_by(City.id.asc())
        .all()
    )
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
