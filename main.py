from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config.ioc import RepositoryConatiner, AsyncContainer, MemberContainer
from src.config.middlewares import SessionMiddleware
from src.config.rdb.driver import get_session
from src.config.rdb.mapper import start_mappers
from src.member.member_controller import member_router
from src.config.settings import lifespan


def create_app() -> FastAPI:
    a = AsyncContainer()
    a.wire(packages=["src"])

    container = RepositoryConatiner(session=get_session())
    container.wire(packages=["src"])

    b = MemberContainer()
    b.wire(packages=["src"])

    app = FastAPI(lifespan=lifespan)

    start_mappers()

    # Controller
    app.include_router(member_router)

    app.add_middleware(SessionMiddleware)

    return app
