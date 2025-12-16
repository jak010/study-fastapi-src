from __future__ import annotations

from dependency_injector.wiring import inject, Provide

from src.config.ioc import RepositoryConatiner
from src.infrastructure.async_member_repository import AsyncMemberRepository


class MemberServiceV2:


    def __init__(self):...
        # self.repository: AsyncMemberRepository = member_repository

    # async def get_member_v2(self, member_id):
    #     r = await self.repository.find_by_member_id(member_id=member_id)
    #
    #     print(r)
