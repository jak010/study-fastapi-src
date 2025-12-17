from dependency_injector.wiring import Provide, inject
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.ioc import AsyncContainer, AsyncSessionProvider


class AsyncTransactional:

    def __init__(self):
        self.s = AsyncSessionProvider.registry()

    @inject
    async def session_factory(
            self,
            async_session: AsyncSession = Provide[AsyncContainer.async_session]
    ):
        return async_session

    def __call__(self, func):
        async def inner(*args, **kwargs):
            print("BEFORE")

            session = await self.session_factory()

            await self.s.add(session)

            r = await func(*args, **kwargs)

            await session.commit()
            await session.close()

            print("AFTER")
            r = 1
            return r

        return inner
