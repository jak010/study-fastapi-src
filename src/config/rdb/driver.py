from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker, Session


def get_url() -> URL:
    return URL.create(
        drivername="mysql+pymysql",
        username='root',
        password="1234",
        database="fastapi",
        host="127.0.0.1",
        port=9901
    )


def get_session() -> Session:
    engine = create_engine(get_url(), echo=True)

    _Session = sessionmaker(bind=engine)
    session = _Session()
    return session
