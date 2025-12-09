from sqlalchemy import Column, Index, MetaData, String, Table, text
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import registry

metadata = MetaData()

t_member = Table(
    'member', metadata,
    Column('member_id', INTEGER(1), primary_key=True),
    Column('email', String(36), nullable=False),
    Column('name', String(12), nullable=False),
    Column('age', SMALLINT(1), server_default=text("'0'")),
    Index('email', 'email', unique=True)
)


def start_mappers():
    from src.member.member_entity import MemberEntity
    mapper_registry = registry()
    mapper_registry.map_imperatively(MemberEntity, t_member)
    return mapper_registry
