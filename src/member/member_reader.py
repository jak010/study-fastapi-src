from abc import ABC, abstractmethod

from src.member.entity.member_entity import MemberEntity


class MemberReader(ABC):

    @abstractmethod
    def find_by_member_id(self, member_id) -> MemberEntity: ...

    @abstractmethod
    def find_by_member_id_with(self, member_id, with_profile) -> MemberEntity:
        """
        Member와 연계된 MemberProfile을 선택적으로 join 하기

        """
        ...
