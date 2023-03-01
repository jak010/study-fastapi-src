from __future__ import annotations

from pydantic import BaseModel, Field, EmailStr


class MemberCreateDto(BaseModel):
    email: EmailStr = Field(title="사용자 이메일")
    name: str = Field(title="사용자 이름")
    age: int = Field(title="사용자 나이")
