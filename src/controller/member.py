from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse

from src.domain.member.service import MemberService
from src.domain.member.data.dto import MemberCreateDto

member_router = APIRouter(
    prefix="/members",
    tags=["members"],
)


@member_router.get("/{reference_id}", description="사용자 조회")
def get_member(
        reference_id: int,
        member_service: MemberService = Depends(MemberService)
):
    member = member_service.find_by_member(reference_id=reference_id)

    if not member:
        return JSONResponse(status_code=404, content={})

    return JSONResponse(status_code=200, content=member.to_dict())


@member_router.post("/", description="사용자 등록")
def create_member(
        member_create_dto: MemberCreateDto,
        member_service: MemberService = Depends(MemberService)
):
    try:
        member = member_service.create_member(member_create_dto)
    except Exception:
        return JSONResponse(status_code=400, content={'msg': "Member Created Failure"})

    return JSONResponse(status_code=200, content={'items': member})
