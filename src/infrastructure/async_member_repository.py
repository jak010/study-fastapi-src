from typing import Optional

from sqlalchemy import insert
from sqlalchemy import select

from src.member.entity.member_entity import MemberEntity
from src.member.member_reader import MemberReader, MemberWriter
from .abstract_repository import AbstractRepository
from ..member.entity import MemberProfileEntity


class AsyncMemberRepository(AbstractRepository, MemberReader, MemberWriter):

    def find_by_member_id_with(self, member_id, with_profile) -> MemberEntity:
        pass

    async def find_by_member_id(self, member_id, with_profile=False) -> Optional[MemberEntity]:
        tables = [MemberEntity]

        if with_profile:
            tables.append(MemberProfileEntity)

        query = select(*tables) \
            .outerjoin(MemberProfileEntity, MemberProfileEntity.member_id == MemberEntity.member_id) \
            .where(MemberEntity.member_id == member_id)

        result = await self.session().execute(query)
        member, member_profile = result.first()  # TODO, 251219 : 조치하기

        return member  # TODO, 251219 : 조치하기

    async def insert(self, name, email) -> MemberEntity:
        sql = insert(MemberEntity).values(name=name, email=email)

        r = await self.session().execute(sql)
        return r
