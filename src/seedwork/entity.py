from __future__ import annotations

import abc


class NotExistEntity(Exception):
    """ Entity가 존재하지 않음 """


class AbstractEntity(metaclass=abc.ABCMeta):
    reference_id = None
