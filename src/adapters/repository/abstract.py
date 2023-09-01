from __future__ import annotations

from abc import ABCMeta


class AbstractRepositry(metaclass=ABCMeta):

    def __init__(self, session):
        self._session = session
