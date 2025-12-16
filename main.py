from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config.ardb.engine import crete_engine, meta
from src.config.ioc import RepositoryConatiner
from src.config.rdb.driver import get_session
from src.config.rdb.mapper import start_mappers
from src.member.member_controller import member_router


def create_app() -> FastAPI:
    container = RepositoryConatiner(session=get_session())
    container.wire(packages=["src"])

    app = FastAPI()

    start_mappers()

    # Controller
    app.include_router(member_router)

    return app
