from __future__ import annotations

from typing import TYPE_CHECKING

from src.config.ardb.transactional import AsyncTransactional
from src.member.exception import MemberNotFound

if TYPE_CHECKING:
    from src.infrastructure.async_member_repository import AsyncMemberRepository
    from src.infrastructure.async_member_profile_repository import AsyncMemberProfileRepository


class MemberServiceV2:
    repository: AsyncMemberRepository

    def __init__(self, member_repository, member_profile_repo):
        self.repository: AsyncMemberRepository = member_repository
        self.member_profile_reposiotry: AsyncMemberProfileRepository = member_profile_repo

    @AsyncTransactional()
    async def get_member_v2(self, member_id):
        member = await self.repository.find_by_member_id(member_id, with_profile=True)
        if member is None:
            raise MemberNotFound()

        print(dir(member))
        print(await member.member_profile)

        return member

    @AsyncTransactional()
    async def update_hit(self, member_id):
        member = await self.repository.find_by_member_id(member_id)
        if member is None:
            raise MemberNotFound()

        await self.member_profile_reposiotry.increment_hit(member.member_id)
