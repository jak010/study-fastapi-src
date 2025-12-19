from sqlalchemy.ext.asyncio import async_scoped_session

from src.config.util import AsyncSessionContext


class AsyncTransactional:

    def __init__(self):
        self.session_manager = None

    def __call__(self, func):
        async def inner(*args, **kwargs):
            async_session: async_scoped_session = AsyncSessionContext.get()

            async with async_session.begin():
                r = await func(*args, **kwargs)

            await async_session.remove()

            return r

        return inner
