from sqlalchemy import Column, MetaData, String, Table, text
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import registry, Session
from sqlalchemy.orm import sessionmaker

from src.db import get_url
from src.domain.member.member_entity import Member as MemberModel

from functools import cached_property

mapper_registry = registry()
metadata = MetaData()

t_member = Table(
    'member', mapper_registry.metadata,
    Column('reference_id', INTEGER(1), primary_key=True),
    Column('name', String(12), nullable=False),
    Column('age', SMALLINT(1), server_default=text("'0'"))
)


def start_mappers():
    mapper_registry.map_imperatively(MemberModel, t_member)


class Context:

    def __init__(self):
        self.engine = create_engine(get_url(), echo=True)

    @cached_property
    def session(self) -> Session:
        _Session = sessionmaker(bind=self.engine)
        session = _Session()
        print(session, id(session))
        return session


if __name__ == '__main__':
    start_mappers()

    member_model = MemberModel(name='ja', age=2)

    conn = Context()
    conn.session.add(member_model)
    conn.session.commit()

    # engine = create_engine(get_url(), echo=True)
    # _Session = sessionmaker(bind=engine)
    # session = _Session()
    # session.add(member_model)
    # session.commit()

    # print(dir(session))
    # print(type(session)) # <class 'sqlalchemy.orm.session.Session'>
