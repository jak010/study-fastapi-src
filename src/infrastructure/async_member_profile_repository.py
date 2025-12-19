from typing import NoReturn

from sqlalchemy import text, select

from src.member.entity.member_profile import MemberProfileEntity
from .abstract_repository import AbstractRepository


class AsyncMemberProfileRepository(AbstractRepository):

    async def find_member_profile_by_member_id(self, member_id) -> MemberProfileEntity:
        query = select(MemberProfileEntity) \
            .where(MemberProfileEntity.member_id == member_id)

        result = await self.session().execute(query)

        return result.scalar()

    async def increment_hit(self, member_id) -> NoReturn:
        sql = text(
            """
            UPDATE fastapi.member_profile
            SET hit = hit+1 
            WHERE member_id= :member_id; 
            """
        )

        params = {
            "member_id": member_id
        }

        await self.session().execute(sql, params)
