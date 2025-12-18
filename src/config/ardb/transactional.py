from dependency_injector.wiring import Provide, inject
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from typing_extensions import assert_never

from src.config.ioc import AsyncContainer
from src.config.util import AsyncSessionContext


class AsyncTransactional:

    def __init__(self):
        self.session_manager = None

    @inject
    async def get_session(
            self,
            async_session: AsyncSession = Provide[AsyncContainer.async_session],
    ):
        return async_session

    @inject
    def get_engine(
            self,
            async_engine: AsyncSession = Provide[AsyncContainer.async_engine],
    ):
        return async_engine

    def __call__(self, func):
        async def inner(*args, **kwargs):
            print("BEFORE")

            async_session: async_scoped_session = AsyncSessionContext.get()

            async with async_session.begin():
                print("TRANSACTION-START")
                r = await func(*args, **kwargs)

                await async_session.commit()

            await async_session.close()

            print("TRANSACTION-COMMIT")

            print("AFTER")

            return r

        return inner
