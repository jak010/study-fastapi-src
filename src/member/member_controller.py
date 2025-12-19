from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Path
from fastapi.routing import APIRouter

from src.config.ioc import RepositoryConatiner, ServiceContainer
from src.contrib.response_model import ResponseBaseModel
from src.member.member_service_v2 import MemberServiceV2

member_router = APIRouter(tags=['Member'])


@member_router.get(path="/member")
@inject
async def member_retreieve(
        service: MemberServiceV2 = Depends(
            Provide[ServiceContainer.member_service]
        ),
) -> ResponseBaseModel:
    r = await service.get_member_v2(member_id=1)

    return ResponseBaseModel(data={})


@member_router.post(path="/member/{member_id}")
@inject
async def member_retreieve(
        member_id =  Path(),
        service: MemberServiceV2 = Depends(
            Provide[ServiceContainer.member_service]
        ),
) -> ResponseBaseModel:
    r = await service.update_hit(member_id=member_id)

    return ResponseBaseModel(data={})
