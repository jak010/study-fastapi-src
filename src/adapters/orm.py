from sqlalchemy import Column, MetaData, String, Table, text, Index
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import registry

mapper_registry = registry()
metadata = MetaData()

t_member = Table(
    'member', metadata,
    Column('reference_id', INTEGER(1), primary_key=True),
    Column('email', String(36), nullable=False, unique=True),
    Column('name', String(12), nullable=False),
    Column('age', SMALLINT(1), server_default=text("'0'")),
    Index('email', 'email', unique=True)
)


def start_mappers():
    from src.domain.member.member_entity import MemberEntity

    mapper_registry.map_imperatively(MemberEntity, t_member)
