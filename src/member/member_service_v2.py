from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from src.config.ardb.transactional import AsyncTransactional

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
        r = await self.repository.find_by_member_id(member_id)

        r2 = await self.member_profile_reposiotry.find_member_profile_by_member_id(r.member_id)

        return 1

    @AsyncTransactional()
    async def update_hit(self, member_id):
        r = await self.repository.find_by_member_id(member_id)

        r2 = await self.member_profile_reposiotry.increment_hit(r.member_id)

        return r