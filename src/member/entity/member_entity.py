from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .member_profile import MemberProfileEntity


@dataclass
class MemberEntity:
    member_id: Optional[int]
    email: str
    name: str
    age: str

    member_profile: MemberProfileEntity = None
