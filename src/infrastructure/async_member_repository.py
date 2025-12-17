from sqlalchemy import text, insert

from src.member.entity.member_entity import MemberEntity
from src.member.member_reader import MemberReader, MemberWriter
from .abstract_repository import AbstractRepository


class AsyncMemberRepository(AbstractRepository, MemberReader, MemberWriter):

    def find_by_member_id_with(self, member_id, with_profile) -> MemberEntity:
        pass

    async def find_by_member_id(self, member_id) -> MemberEntity:
        sql = text("select * from member where member_id = :member_id;")
        params = {
            "member_id": member_id
        }

        result = await self.fetchone(sql, params)

        return result

    async def insert(self, name, email) -> MemberEntity:
        sql = insert(MemberEntity).values(name=name, email=email)

        await self.execute(sql)
