from __future__ import annotations

from fastapi import FastAPI

from src.config.ioc import RepositoryConatiner
from src.config.rdb.driver import get_session
from src.config.rdb.mapper import start_mappers


def create_app() -> FastAPI:
    container = RepositoryConatiner(session=get_session())
    container.wire(packages=["src"])

    app = FastAPI()

    start_mappers()

    # Controller
    from src.member.member_controller import member_router
    app.include_router(member_router)

    return app


app = create_app()
