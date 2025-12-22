from dependency_injector import providers, containers


class AsyncContainer(containers.DeclarativeContainer):
    from src.config.ardb.engine import session_factory, crete_engine

    async_engine = providers.Singleton(crete_engine)
    async_session = providers.Factory(session_factory, engine=async_engine)


class RepositoryConatiner(containers.DeclarativeContainer):
    from src.config.rdb.driver import get_session
    session = providers.Singleton(get_session)



class MemberContainer(containers.DeclarativeContainer):
    # Repository
    from src.infrastructure.async_member_repository import AsyncMemberRepository
    async_member_repository = providers.Factory(
        AsyncMemberRepository,
        async_session=AsyncContainer.async_session
    )

    # Service
    from src.member.member_service_v2 import MemberService
    member_service = providers.Factory(
        MemberService,
        member_repository=async_member_repository
    )
