from os import getenv

import asyncpg
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class GetCounterCountResponse(BaseModel):
    count: int


@router.get("/counter/count")
async def get_counter_count() -> GetCounterCountResponse:
    conn = await asyncpg.connect(getenv("DATABASE_URL"))
    count: int = await conn.fetchval("SELECT COUNT(1) FROM access_log")
    conn.close()
    return GetCounterCountResponse(count=count)


class PostCounterIncrementResponse(BaseModel):
    count: int


@router.post("/counter/increment")
async def post_counter_increment() -> PostCounterIncrementResponse:
    conn = await asyncpg.connect(getenv("DATABASE_URL"))
    await conn.execute("INSERT INTO access_log DEFAULT VALUES")
    count: int = await conn.fetchval("SELECT COUNT(1) FROM access_log")
    conn.close()
    return PostCounterIncrementResponse(count=count)
