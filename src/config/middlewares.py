from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from src.config.ioc import AsyncContainer
from src.config.util import AsyncSessionContext


class SessionMiddleware(BaseHTTPMiddleware):

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint,
    ) -> Response:
        async_session = AsyncContainer.async_session()

        _session = AsyncSessionContext.set(async_session)

        response = await call_next(request)
        response.headers["X-Custom-Header"] = "CustomValue"

        AsyncSessionContext.reset(_session)

        return response
