from sqlalchemy.ext.asyncio import async_scoped_session

from src.config.util import AsyncSessionContext


class AsyncTransactional:

    def __init__(self):
        self.session_manager = None

    def __call__(self, func):
        async def inner(*args, **kwargs):
            async_session: async_scoped_session = AsyncSessionContext.get()
            print(f"Transactional : {async_session}")
            async with async_session.begin():
                r = await func(*args, **kwargs)

            await async_session.remove()
            await async_session.close()

            return r

        return inner
