# from __future__ import annotations

from typing import TypeVar

from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from fastapi.routing import APIRouter

from src.config.ioc import RepositoryConatiner
from src.contrib.response_model import ResponseBaseModel

member_router = APIRouter(tags=['Member'])

T = TypeVar("T")


@member_router.get(path="/member")
@inject
async def member_retreieve(
        # service: MemberServiceV2 = Depends(MemberServiceV2),
        repository=Depends(
            Provide[RepositoryConatiner.async_member_repository]
        )
) -> ResponseBaseModel:
    # service.get_member(member_id=1)

    result = await repository.find_by_member_id(member_id=1)

    print(result)

    # await service.get_member_v2(member_id=1)

    return ResponseBaseModel(data={})
