from __future__ import annotations

from fastapi import Depends, Body
from fastapi.responses import JSONResponse
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from src.domain.member.member_service import MemberService

member_router = InferringRouter(tags=['Member'])


@cbv(member_router)
class MemberController:
    member_service: MemberService = Depends(MemberService)

    @member_router.get("/member", description="멤버 목록조회")
    def list(self):
        return JSONResponse(status_code=200, content={})

    @member_router.post("/member", description="멤버 생성")
    def register(
            self,
            member_id: str = Body(embed=True)
            # name: str = Body(embed=True, min_length=1, max_length=25),
            # age: int = Body(embed=True),
            # email: str = Body(embed=True, min_length=1, max_length=25)
    ):
        member = self.member_service.find_by_member(
            member_id=member_id
        )

        # try:
        #     member = self.member_service.create_member(member_create_dto)
        # except Exception:
        #     return JSONResponse(status_code=400, content={'msg': "Member Created Failure"})

        # return JSONResponse(status_code=200, content={'items': member})
        return JSONResponse(status_code=200, content={})


@cbv(member_router)
class MemberDetailController:

    @member_router.get("/member/{member_id}", description="사용자 상세 조회")
    def retreieve(
            self,
            member_id: int,
            member_service: MemberService = Depends(MemberService)
    ):
        member = member_service.find_by_member(reference_id=member_id)

        if not member:
            return JSONResponse(status_code=404, content={})

        return JSONResponse(status_code=200, content=member.to_dict())

    @member_router.put("/member/{member_id}", description="사용자 업데이트")
    def update(self):
        return JSONResponse(status_code=200, content={})

    @member_router.delete("/member/{member_id}", description="사용자 삭제하기")
    def delete(self):
        return JSONResponse(status_code=200, content={})
