#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa """
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sys import agrv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
