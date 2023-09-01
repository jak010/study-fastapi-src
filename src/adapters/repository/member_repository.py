from __future__ import annotations

from src.adapters.repository.abstract import AbstractRepositry


class MemberRepoitory(AbstractRepositry):

    def get_member(self, member_id):
        sql = "SELECT * FROM member WHERE member_id=:member_id;"
        self._session.execute(sql)

        return self._session.fetchone()
