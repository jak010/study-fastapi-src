from sqlalchemy.orm import registry, relationship

from .orm import Member, MemberProfile

from .orm import metadata


def start_mappers():
    from src.member.entity import MemberEntity, MemberProfileEntity

    mapper_registry = registry(metadata=metadata)  # metadata 지정 안해주면 밑의 속성 매핑 동작안함
    mapper_registry.map_imperatively(MemberProfileEntity, MemberProfile.__table__)

    mapper_registry.map_imperatively(
        MemberEntity, Member.__table__,
        properties={
            'member_profile': relationship(
                MemberProfileEntity,
                primaryjoin=(
                    'member.c.member_id == foreign(member_profile.c.member_id)'
                ),
                lazy='joined',
                uselist=False
            )
        }
    )

    return mapper_registry
