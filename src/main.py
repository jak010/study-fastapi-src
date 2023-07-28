from __future__ import annotations

from fastapi import Body, FastAPI, Request, Response

from src.adapters.orm import start_mappers


# @app.middleware("http")
# def middleware(request: Request, call_next):
#     print("current:", request)
#     print(dir(request))
#     print(request.url)
#     response = call_next(request)
#
#     return response


def create_app() -> FastAPI:
    app = FastAPI()

    start_mappers()

    # Controller
    from src.controller.member import member_router
    from src.controller.profile import profile_router
    app.include_router(member_router)
    app.include_router(profile_router)

    return app
