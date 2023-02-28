from __future__ import annotations

from fastapi import FastAPI

from .orm import start_mappers


def create_app() -> FastAPI:
    print(start_mappers())
    app = FastAPI()

    # Controller
    from src.controller.member import member_router
    app.router.include_router(member_router)

    return app
