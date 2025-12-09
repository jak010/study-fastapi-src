from typing import Optional
import datetime

from sqlalchemy import Date, DateTime, Index, String, text
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declarative_base

Base = declarative_base()

metadata = Base.metadata


class Member(Base):
    __tablename__ = 'member'
    __table_args__ = (
        Index('email', 'email', unique=True),
    )

    member_id: Mapped[int] = mapped_column(INTEGER(1), primary_key=True)
    email: Mapped[str] = mapped_column(String(36), nullable=False)
    name: Mapped[str] = mapped_column(String(12), nullable=False)
    age: Mapped[Optional[int]] = mapped_column(SMALLINT(1), server_default=text("'0'"))


class MemberProfile(Base):
    __tablename__ = 'member_profile'

    member_id: Mapped[int] = mapped_column(INTEGER(1), primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    birth_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))