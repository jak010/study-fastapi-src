from sqlalchemy.orm import joinedload

from src.member.entity.member_entity import MemberEntity
from src.member.member_reader import MemberReader


class MemberRepository(MemberReader):

    def __init__(self, session):
        self.session = session

    def find_by_member_id(self, member_id) -> MemberEntity:
        return self.session.query(MemberEntity).filter_by(member_id=member_id).first()

    def find_by_member_id_with(self, member_id, with_profile) -> MemberEntity:
        query = self.session.query(MemberEntity).filter_by(member_id=member_id)

        if with_profile:
            query = query.options(joinedload(MemberEntity.member_profile))

        return query.first()
