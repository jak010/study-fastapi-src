from __future__ import annotations

from src.config.ioc import RepositoryConatiner
from src.member.member_reader import MemberReader

from dependency_injector.wiring import Provide


class MemberService:
    member_reader: MemberReader = Provide[RepositoryConatiner.member_repository]

    def get_member(self, member_id):
        member = self.member_reader.find_by_member_id(member_id=member_id)
        print(member)
