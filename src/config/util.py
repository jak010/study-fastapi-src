from contextvars import ContextVar

AsyncSessionContext: ContextVar[int] = ContextVar("AsyncSessionContext")
