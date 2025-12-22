from typing import Optional

from sqlalchemy import insert, ChunkedIteratorResult
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.member.entity.member_entity import MemberEntity
from src.member.i_member_store import MemberReader, MemberWriter
from .abstract_repository import AbstractRepository


class AsyncMemberRepository(AbstractRepository, MemberReader, MemberWriter):

    async def find_by_member_id(self, member_id) -> MemberEntity:
        query = select(MemberEntity) \
            .where(MemberEntity.member_id == member_id)

        result = await self.session().exeucte(query)

        return result.scalar.one()

    async def find_by_member_with_profile(
            self,
            member_id
    ) -> Optional[MemberEntity]:
        query = select(MemberEntity) \
            .options(joinedload(MemberEntity.member_profile)) \
            .where(MemberEntity.member_id == member_id)

        result: ChunkedIteratorResult = await self.session().execute(query)

        return result.scalar()

    async def insert(self, name, email) -> MemberEntity:
        sql = insert(MemberEntity).values(name=name, email=email)

        r = await self.session().execute(sql)
        return r
