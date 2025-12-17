from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from src.config.ardb.transactional import AsyncTransactional

if TYPE_CHECKING:
    from src.infrastructure.async_member_repository import AsyncMemberRepository


class MemberServiceV2:
    repository: AsyncMemberRepository

    def __init__(self, member_repository):
        self.repository: AsyncMemberRepository = member_repository

    @AsyncTransactional()
    async def get_member_v2(self, member_id):
        r = await self.repository.find_by_member_id(member_id)

        c = str(uuid.uuid4().hex)
        name = c[0:4]
        email = f"{c[0:4]}@test.com"
        r = await self.repository.insert(name, email)

        return r
