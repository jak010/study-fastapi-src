from dependency_injector import providers, containers

from src.config.ardb.session_registry import SessionQueue


class AsyncContainer(containers.DeclarativeContainer):
    from src.config.ardb.engine import get_db, crete_engine

    async_engine = providers.Singleton(crete_engine)

    async_session = providers.Resource(get_db, engine=async_engine)


class AsyncSessionProvider(containers.DeclarativeContainer):

    registry = providers.Singleton(SessionQueue)



class RepositoryConatiner(containers.DeclarativeContainer):
    from src.config.rdb.driver import get_session
    from src.infrastructure.member_repository import MemberRepository
    session = providers.Singleton(get_session)
    member_repository = providers.Singleton(
        MemberRepository,
        session=session
    )

    from src.infrastructure.async_member_repository import AsyncMemberRepository

    async_member_repository = providers.Factory(
        AsyncMemberRepository,
        async_session=AsyncContainer.async_session
    )


class ServiceContainer(containers.DeclarativeContainer):
    from src.member.member_service_v2 import MemberServiceV2
    member_service = providers.Factory(
        MemberServiceV2,
        member_repository=RepositoryConatiner.async_member_repository
    )
