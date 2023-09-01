from __future__ import annotations

from fastapi import Body, FastAPI, Request, Response
from src.config.ioc import RepositoryConatiner


# @app.middleware("http")
# def middleware(request: Request, call_next):
#     print("current:", request)
#     print(dir(request))
#     print(request.url)
#     response = call_next(request)
#
#     return response


def create_app() -> FastAPI:
    container = RepositoryConatiner()
    container.wire(packages=[
        ".service_layer"
    ])

    app = FastAPI()
    # app.container = container

    # Controller
    from src.controller.member import member_router
    from src.controller.profile import profile_router
    app.include_router(member_router)
    # app.include_router(profile_router)

    return app
