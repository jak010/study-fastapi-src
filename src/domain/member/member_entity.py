from __future__ import annotations

import json

# from src.seedwork.entity import AbstractEntity

from dataclasses import dataclass
from typing import Optional


@dataclass
class MemberEntity:
    member_id: Optional[int]
    email: str
    name: str
    age: str
