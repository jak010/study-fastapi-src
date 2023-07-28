from __future__ import annotations

from typing import Optional

from src.domain.member.member_entity import MemberEntity
from src.seedwork.entity import NotExistEntity
from src.seedwork.repository import SqlAlchemyRepositoy


class MemberRepositoy(SqlAlchemyRepositoy):

    def get_by_id(self, reference_id: int) -> MemberEntity:
        query = self.uow.session.query(MemberEntity) \
            .filter(MemberEntity.reference_id == reference_id)
        member = query.one_or_none()

        if member:
            return member

        raise NotExistEntity("NotExsit Member")

    def find_by_id(self, reference_id: int) -> Optional[MemberEntity]:
        query = self.uow.session.query(MemberEntity) \
            .filter(MemberEntity.reference_id == reference_id)

        return query.one_or_none()

    def save(self, member_entity: MemberEntity):
        self.uow.session.add(member_entity)
        self.uow.session.commit()
