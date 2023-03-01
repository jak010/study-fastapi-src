from __future__ import annotations

import abc

from functools import cached_property

from src.adapters.db import get_session


class AbstractUnitofWork(metaclass=abc.ABCMeta):

    def __enter__(self) -> AbstractUnitofWork:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.rollback()

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplemented

    @abc.abstractmethod
    def rollback(self):
        raise NotImplemented

    @property
    @abc.abstractmethod
    def session(self): ...


class SqlAlchemyUnitOfWork(AbstractUnitofWork):

    def __init__(self):
        self._session = get_session()

    @cached_property
    def session(self):
        return self._session

    def __enter__(self):
        return super(SqlAlchemyUnitOfWork, self).__enter__()

    def __exit__(self, *args):
        self._session.commit()
        self._session.close()

    def _commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
