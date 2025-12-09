from __future__ import annotations

from typing import TypeVar

from fastapi import Depends
from fastapi.routing import APIRouter

from src.contrib.response_model import ResponseBaseModel
from src.member.member_service import MemberService

member_router = APIRouter(tags=['Member'])

T = TypeVar("T")


@member_router.get(path="/member")
async def member_retreieve(
        service: MemberService = Depends(MemberService)
) -> ResponseBaseModel:
    service.get_member(member_id=1)

    return ResponseBaseModel(data={})
