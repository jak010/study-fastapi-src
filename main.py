from __future__ import annotations

from fastapi import FastAPI

from src.config.ioc import RepositoryConatiner, AsyncContainer, ServiceContainer
from src.config.rdb.driver import get_session
from src.config.rdb.mapper import start_mappers
from src.member.member_controller import member_router


def create_app() -> FastAPI:
    a = AsyncContainer()
    a.wire(packages=["src"])

    b = ServiceContainer()
    b.wire(packages=["src"])

    container = RepositoryConatiner(session=get_session())
    container.wire(packages=["src"])

    app = FastAPI()

    start_mappers()

    # Controller
    app.include_router(member_router)

    return app
