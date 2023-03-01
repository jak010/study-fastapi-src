from __future__ import annotations

from fastapi import APIRouter

from fastapi.responses import JSONResponse

from src.domain.member.data.dto import MemberCreateDto
from src.domain.member.usecase.member_create import MemberCreate

member_router = APIRouter(
    prefix="/members",
    tags=["members"],
)


@member_router.post("/", description="사용자 등록하기")
def register_member(member_create_dto: MemberCreateDto):
    MemberCreate(member_create_dto=member_create_dto) \
        .create_member()

    return JSONResponse(
        status_code=201,
        content={
            "msg": "member create success"
        }
    )
