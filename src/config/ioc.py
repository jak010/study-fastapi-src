from dependency_injector import providers, containers

from src.config.rdb.driver import get_session
from src.infrastructure.member_repository import MemberRepository


class RepositoryConatiner(containers.DeclarativeContainer):
    session = providers.Singleton(get_session)

    member_repository = providers.Singleton(MemberRepository, session=session)
