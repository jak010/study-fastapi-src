from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Path
from fastapi.routing import APIRouter

from src.config.ioc import MemberContainer
from src.contrib.response_model import ResponseBaseModel
from src.member.dto.member import MemberDto
from src.member.member_service_v2 import MemberService

member_router = APIRouter(tags=['Member'])


@member_router.get(
    path="/member",
    response_model=ResponseBaseModel[MemberDto]
)
@inject
async def member_retreieve(
        service: MemberService = Depends(
            Provide[MemberContainer.member_service]
        ),
) -> ResponseBaseModel:
    member = await service.get_member_v2(member_id=2)

    return ResponseBaseModel(data=MemberDto.of(member))


@member_router.post(path="/member/{member_id}")
@inject
async def member_retreieve(
        member_id=Path(),
        service: MemberService = Depends(
            Provide[MemberContainer.member_service]
        ),
) -> ResponseBaseModel:
    r = await service.update_hit(member_id=member_id)

    return ResponseBaseModel(data={})
