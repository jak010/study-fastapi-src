from functools import lru_cache

import aiomysql
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from sqlalchemy import URL


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
        echo=True,
        pool_size=10,
        max_overflow=20,
        pool_timeout=30,
        pool_recycle=1800
    )


async def get_db() -> AsyncSession:
    engine = crete_engine()

    async_session = async_sessionmaker(
        engine,
        autoflush=False,
        autocommit=False,
        class_=AsyncSession
    )

    async with async_session() as session:
        yield session


class DBProvider:
    """
    https://python-dependency-injector.ets-labs.org/providers/async.html
    """
    ...
