from dataclasses import dataclass


@dataclass
class MemberProfileEntity:
    member_id: int
    phone: str = None
    birth_date: str = None
    created_at: str = None
    updated_at: str = None
