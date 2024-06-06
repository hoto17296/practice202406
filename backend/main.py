from os import getenv

from fastapi import FastAPI
from views import router

DEBUG = bool(int(getenv("DEBUG", "0")))

app = FastAPI(
    docs_url="/api/docs" if DEBUG else None,
    redoc_url=None,
    openapi_url="/api/openapi.json" if DEBUG else None,
)

app.include_router(router, prefix="/api")
