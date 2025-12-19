import asyncio
from functools import lru_cache

from sqlalchemy import MetaData
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    async_scoped_session
)


def get_url() -> URL:
    return URL.create(
        drivername="mysql+aiomysql",
        username='root',
        password="1234",
        database="fastapi",
        host="127.0.0.1",
        port=9901
    )


meta = MetaData()


@lru_cache(maxsize=1)
def crete_engine():
    return create_async_engine(
        get_url(),
        echo=False,
        pool_size=30,
        max_overflow=10,
        pool_timeout=30,
        pool_recycle=1800,
        pool_pre_ping=True
    )


def session_factory(engine) -> async_scoped_session:
    _session = async_sessionmaker(
        engine,
        autoflush=False,
        autocommit=False,
        class_=AsyncSession,
        expire_on_commit=False,

    )

    _async_scoped_session = async_scoped_session(
        session_factory=_session,
        scopefunc=asyncio.current_task
    )

    return _async_scoped_session
