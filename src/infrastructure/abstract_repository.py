from sqlalchemy.ext.asyncio import async_scoped_session

from src.config.util import AsyncSessionContext


class AbstractRepository:

    def __init__(self, async_session):
        self.session: async_scoped_session = AsyncSessionContext.get()
