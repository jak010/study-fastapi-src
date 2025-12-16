from __future__ import annotations

from dependency_injector.wiring import Provide
from sqlalchemy import text

from src.config.ioc import RepositoryConatiner
from src.config.rdb.transactional import Transactional
from src.member.member_reader import MemberReader


class MemberService:
    member_reader: MemberReader = Provide[RepositoryConatiner.member_repository]

    @Transactional
    def get_member(self, member_id):
        member = self.member_reader.find_by_member_id_with(member_id=member_id, with_profile=True)
        return member

    async def get_member_v2(self, name, db):
        raw_sql = text("select * from member where member_id=1;")
        result = await db.execute(raw_sql)

        # print(result.mappings().all())
        # print(result.mappings().fetchone())

        await db.commit()
