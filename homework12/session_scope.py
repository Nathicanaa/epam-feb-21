from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()


@contextmanager
def session_scope() -> Session:
    """Provide a transactional scope around a series of operations.
    This context manager example has been taken from sqlalchemy documentation"""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
