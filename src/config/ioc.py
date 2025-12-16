from dependency_injector import providers, containers

from src.config.ardb.engine import get_db
from src.config.rdb.driver import get_session
from src.infrastructure.async_member_repository import AsyncMemberRepository
from src.infrastructure.member_repository import MemberRepository


class AsyncContainer(containers.DeclarativeContainer):
    async_session = providers.Resource(get_db)


class RepositoryConatiner(containers.DeclarativeContainer):
    session = providers.Singleton(get_session)
    member_repository = providers.Singleton(
        MemberRepository,
        session=session
    )

    async_member_repository = providers.Factory(
        AsyncMemberRepository,
        async_session=AsyncContainer.async_session
    )
