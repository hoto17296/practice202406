from os import getenv

import asyncpg
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class GetCounterResponse(BaseModel):
    count: int


@router.get("/counter")
async def get_counter() -> GetCounterResponse:
    conn = await asyncpg.connect(getenv("DATABASE_URL"))
    await conn.execute("INSERT INTO access_log DEFAULT VALUES")
    count: int = await conn.fetchval("SELECT COUNT(1) FROM access_log")
    conn.close()
    return GetCounterResponse(count=count)
