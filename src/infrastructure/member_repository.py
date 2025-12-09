from src.member.member_entity import MemberEntity


class MemberRepository:

    def __init__(self, session):
        self.session = session

    def find_by_member_id(self, member_id) -> MemberEntity:
        return self.session.query(MemberEntity).filter_by(member_id=member_id).first()
