from abc import ABCMeta

from src.adapters.db import get_session
from src.config.ioc import RepositoryConatiner
from dependency_injector.wiring import Provide, inject, Provider
from dependency_injector.containers import DynamicContainer


class AbstractUniofWork(metaclass=ABCMeta): ...


class SqlalchemyUnitofWork(AbstractUniofWork):

    def __init__(self):
        self._session = get_session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.commit()
        self._session.close()

    @property
    @inject
    def repository(self, repo=Provide[RepositoryConatiner]) -> RepositoryConatiner:
        # print(type(repo))
        # print(dir(repo))
        from dependency_injector.containers import DynamicContainer
        print("="*10)
        print(type(repo), dir(repo))
        print("=" * 10)
        repo.session = self._session

        # repo.session = get_session()
        #
        return repo
