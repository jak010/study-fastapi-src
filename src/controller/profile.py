from fastapi.responses import JSONResponse
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

profile_router = InferringRouter(tags=['Profile'])


@cbv(profile_router)
class ProfileController:

    @profile_router.get(path="/member/{member_id}/profile")
    def get(self):
        return JSONResponse(status_code=200, content={})
