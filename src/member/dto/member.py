from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, PrivateAttr

from src.member.entity import MemberEntity


class MemberProfileDto(BaseModel):
    phone: Optional[str]
    hit: Optional[int]
    birth_date: Optional[str]

    _member_id: int = PrivateAttr()

    @classmethod
    def of(cls, entity):
        return cls(
            phone=entity.phone,
            hit=entity.hit,
            birth_date=entity.birth_date.isoformat(),
            _member_id=entity.member_id
        )


class MemberDto(BaseModel):
    member_id: int
    email: str
    name: str
    age: int

    profile: Optional[MemberProfileDto]

    @classmethod
    def of(cls, entity: MemberEntity):
        if entity.member_profile:
            profile = MemberProfileDto.of(entity.member_profile)
        else:
            profile = None

        return cls(
            member_id=entity.member_id,
            email=entity.email,
            name=entity.name,
            age=entity.age,
            profile=profile
        )
