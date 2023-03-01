from __future__ import annotations

from src.domain.member.data.dto import MemberCreateDto
from src.domain.member.data.repositoy import MemberRepositoy
from src.domain.member.data.value_object.email import EmailVo
from src.domain.member.entity.member_entity import MemberEntity


class MemberCreate:
    repository = MemberRepositoy()

    def __init__(self, member_create_dto: MemberCreateDto):
        _email_vo = EmailVo(email=member_create_dto.email)

        self._member_entity = MemberEntity(
            email=_email_vo.email,
            name=member_create_dto.name,
            age=member_create_dto.age
        )

    def create_member(self):
        """ 사용자 등록하기 """
        self.repository.add(self._member_entity)
