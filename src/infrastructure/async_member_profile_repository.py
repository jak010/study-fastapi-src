from sqlalchemy import text

from src.member.entity.member_profile import MemberProfileEntity
from .abstract_repository import AbstractRepository


class AsyncMemberProfileRepository(AbstractRepository):

    async def session_check(self):
        test = text("select * from member;")
        r = await self.session().execute(test)
        return r

    async def find_member_profile_by_member_id(self, member_id) -> MemberProfileEntity:
        sql = text("select * from member_profile where member_id = :member_id;")
        params = {
            "member_id": member_id
        }

        result = await self.session().execute(sql, params)

        return MemberProfileEntity.of(**result.mappings().fetchone())
