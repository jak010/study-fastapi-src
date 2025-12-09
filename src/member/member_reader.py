from abc import ABCMeta, abstractmethod

from src.member.member_entity import MemberEntity


class MemberReader(ABCMeta):

    @abstractmethod
    def find_by_member_id(self, member_id) -> MemberEntity: ...
