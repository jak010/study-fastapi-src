from __future__ import annotations

from typing import Optional

from src.domain.member.entity.member_entity import MemberEntity
from src.seedwork.entity import NotExistEntity
from src.seedwork.repository import SqlAlchemyRepositoy


class MemberRepositoy(SqlAlchemyRepositoy):

    def get_by_id(self, reference_id: int) -> Optional[MemberEntity]:
        query = self.uow.session.query(MemberEntity) \
            .filter(MemberEntity.reference_id == reference_id)
        member = query.one_or_none()

        if member:
            return member

        raise NotExistEntity("NotExsit MEMBER")
