from dependency_injector import providers, containers

from src.infrastructure.member_repository import MemberRepository


class RepositoryConatiner(containers.DeclarativeContainer):
    session = providers.Dependency()

    member_repository = providers.Singleton(MemberRepository, session=session)
