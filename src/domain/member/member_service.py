from __future__ import annotations

from src.domain.member.member_entity import MemberEntity
from src.domain.member.member_repositoy import MemberRepositoy


class MemberService:
    member_repository = MemberRepositoy()

    def find_by_member(self, member_id: str):
        z = self.member_repository.find_by_id(member_id=member_id)
        return z

    # def create_member(self, email, age, name):
    #     self.repository.save(MemberEntity(
    #         email=email,
    #         age=age,
    #         name=name
    #     ))
