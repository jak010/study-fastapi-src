from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

from src.config.ardb.transactional import AsyncTransactional
from src.member.entity import MemberProfileEntity, MemberEntity
from src.member.exception import MemberNotFound

if TYPE_CHECKING:
    from src.infrastructure.async_member_repository import AsyncMemberRepository


class MemberService:

    def __init__(self, member_repository):
        self.repository: AsyncMemberRepository = member_repository

    @AsyncTransactional()
    async def get_member_v2(self, member_id) -> MemberEntity:
        member = await self.repository.find_by_member_with_profile(member_id=member_id)
        if member is None:
            raise MemberNotFound()

        return member

    @AsyncTransactional()
    async def update_hit(self, member_id):
        member = await self.repository.find_by_member_id(member_id)
        if member is None:
            raise MemberNotFound()
