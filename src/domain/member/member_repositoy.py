from __future__ import annotations

from typing import Optional

from src.domain.member.member_entity import MemberEntity
from src.seedwork.entity import NotExistEntity
from src.seedwork.repository import SqlAlchemyRepositoy

from src.seedwork.uow import SqlAlchemyQueryUow


class MemberRepositoy:

    def find_by_id(self, member_id: str) -> MemberEntity | NotExistEntity:
        sql = "select * from member where member_id = :member_id;"
        kwargs = {"member_id": member_id}

        with SqlAlchemyQueryUow(sql, kwargs) as uow:
            member = uow.mappings().one_or_none()
            if member:
                return MemberEntity(**member)

            raise NotExistEntity("Not Exist Member")
