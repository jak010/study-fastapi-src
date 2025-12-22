from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MemberProfileEntity:
    member_id: int
    phone: str = None
    hit: int = None
    birth_date: datetime = None
    created_at: str = None
    updated_at: str = None

    @classmethod
    def of(cls,
           member_id: int,
           phone: Optional[str] = None,
           hit: int = None,
           birth_date: Optional[str] = None,
           created_at: Optional[str] = None,
           updated_at: Optional[str] = None
           ) -> MemberProfileEntity:
        return cls(
            member_id=member_id,
            phone=phone,
            hit=hit,
            birth_date=birth_date,
            created_at=created_at,
            updated_at=updated_at
        )
