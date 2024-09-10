from contextlib import asynccontextmanager
from os import getenv

from database import db
from fastapi import FastAPI
from views import router

DEBUG = bool(int(getenv("DEBUG", "0")))


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()


app = FastAPI(
    lifespan=lifespan,
    docs_url="/api/docs" if DEBUG else None,
    redoc_url=None,
    openapi_url="/api/openapi.json" if DEBUG else None,
)

app.include_router(router, prefix="/api")
