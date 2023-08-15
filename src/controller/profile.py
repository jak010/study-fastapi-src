import time

import asyncio

from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute, APIRouter

profile_router = APIRouter()


@profile_router.get("/profile/aio")
async def aio_get_profile():
    # time.sleep(10)
    await asyncio.sleep(10)
    print("Asynchronous")

    return {"pong": 1}


@profile_router.get("/profile")
def get_profile():
    print("Synchronous")

    return {"pong": 1}


@profile_router.get("/profile/{profile_id:path}")
def get_profile2(profile_id):
    print(profile_id, type(profile_id))

    return {"pong": 1}

# @View(router=profile_router, path="/profile")
# class ProfileController:
#
#     def get(self):
#         return JSONResponse(content={}, status_code=200)

# @profile_router.get(path="/member/{member_id}/profile")
# def get(self):
#     return JSONResponse(status_code=200, content={})
