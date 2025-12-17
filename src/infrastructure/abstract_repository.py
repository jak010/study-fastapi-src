from functools import cached_property

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.config.ardb.session_registry import SessionQueue
from src.config.ioc import AsyncSessionProvider


class AbstractRepository:

    def __init__(self, async_session):
        # self.async_session: AsyncSession = AsyncSessionProvider.registry
        self.async_session: SessionQueue = AsyncSessionProvider.registry()

        self._current_session = None

    async def get_session(self) -> AsyncSession:
        if self._current_session is None:
            self._current_session = await self.async_session.get()

        return self._current_session

    async def _execute(self, stmt, params=None):
        session = await self.get_session()
        return await session.execute(stmt, params)

    async def fetchone(self, sql, params=None):
        result = await self._execute(sql, params)
        return result.mappings().fetchone()

    async def fetchall(self, sql, params=None):
        result = await self._execute(sql, params)
        return result.mappings().fetchall()

    async def execute(self, orm):
        return await self._execute(orm)