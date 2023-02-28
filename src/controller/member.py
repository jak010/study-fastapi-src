from typing import Union
from pydantic import BaseModel

from fastapi import APIRouter, Depends

from src.db import Connection
from src.domain.member.member_entity import Member

member_router = APIRouter(
    prefix="/members",
    tags=["members"],
)

in_memory_db = {}


class MemberRegister(BaseModel):
    name: str
    age: int


@member_router.get("/")
def get_member():
    member = Member(age=12, name="kojian")

    conn = Connection()
    conn.session.add(member)
    conn.session.flush(member)
    conn.session.commit()

    return in_memory_db


@member_router.post("/")
def register_member(data: MemberRegister):
    in_memory_db[data.name] = data.age
    return in_memory_db
