from __future__ import annotations

from src.domain.member.data.dto import MemberCreateDto
from src.domain.member.entity.member_entity import MemberEntity
from src.domain.member.repositoy import MemberRepositoy


class MemberService:

    def __init__(self):
        self.repository = MemberRepositoy()

    def find_by_member(self, reference_id: int):
        return self.repository.find_by_id(reference_id=reference_id)

    def create_member(self, member_create_dto: MemberCreateDto):
        self.repository.save(MemberEntity(
            email=member_create_dto.email,
            age=member_create_dto.age,
            name=member_create_dto.name
        ))
