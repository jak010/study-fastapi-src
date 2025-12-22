from abc import ABC, abstractmethod

from src.member.entity.member_entity import MemberEntity


class MemberReader(ABC):

    @abstractmethod
    def find_by_member_id(self, member_id) -> MemberEntity: ...

    @abstractmethod
    def find_by_member_with_profile(self, member_id) -> MemberEntity:
        """
        Member와 연계된 MemberProfile을 선택적으로 join 하기

        """
        ...


class MemberWriter(ABC):

    @abstractmethod
    async def insert(self, name, email): ...
