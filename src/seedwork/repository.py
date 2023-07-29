from __future__ import annotations

import abc

from src.seedwork.entity import AbstractEntity
from src.seedwork.uow import AbstractUoW, SqlAlchemyUnitOfWork, SqlAlchemyQueryUow


class AbstarctRepositoy(metaclass=abc.ABCMeta):
    uow: SqlAlchemyUnitOfWork

    @abc.abstractmethod
    def add(self, entity: AbstractEntity):
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, entity: AbstractEntity):
        raise NotImplementedError()


class SqlAlchemyRepositoy(AbstarctRepositoy):
    uow = SqlAlchemyUnitOfWork()

    def add(self, entity: AbstractEntity):
        with self.uow:
            new_entity = self.uow.session.add(entity)
            return new_entity

    def remove(self, entity: AbstractEntity):
        with self.uow:
            self.uow.session.delete(entity)
