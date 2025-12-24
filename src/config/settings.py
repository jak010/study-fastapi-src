import asyncio
from contextlib import asynccontextmanager

from dependency_injector.wiring import inject, Provide
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine

from src.config.ioc import AsyncContainer


@inject
@asynccontextmanager
async def lifespan(
        app: FastAPI,
        engine: AsyncEngine = Provide[AsyncContainer.async_engine]

):
    # Load the ML model
    print("START")
    yield

    # Clean up the ML models and release the resources
    await engine.dispose()

    print("CLEANUP")
