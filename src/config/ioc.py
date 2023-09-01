from dependency_injector import providers, containers

from src.adapters.repository.member_repository import MemberRepoitory


class RepositoryConatiner(containers.DeclarativeContainer):
    session = providers.Dependency()

    member_repository = providers.Factory(MemberRepoitory, session)
