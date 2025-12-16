from sqlalchemy import text

from sqlalchemy.ext.asyncio import AsyncSession

from src.member.entity.member_entity import MemberEntity
from src.member.member_reader import MemberReader


class AsyncMemberRepository(MemberReader):

    def __init__(self, async_session):
        self.async_session: AsyncSession = async_session

    def find_by_member_id_with(self, member_id, with_profile) -> MemberEntity:
        pass

    async def find_by_member_id(self, member_id) -> MemberEntity:
        sql = text("select * from member where member_id=1;")

        result = await self.async_session.execute(sql)

        return result.mappings().fetchone()
