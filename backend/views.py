from database import db
from fastapi import APIRouter
from prisma import Prisma
from pydantic import BaseModel

router = APIRouter()


class GetCounterCountResponse(BaseModel):
    count: int


@router.get("/counter/count")
async def get_counter_count() -> GetCounterCountResponse:
    async with Prisma() as db:
        count = await db.access_log.count()
    return GetCounterCountResponse(count=count)


class PostCounterIncrementResponse(BaseModel):
    count: int


@router.post("/counter/increment")
async def post_counter_increment() -> PostCounterIncrementResponse:
    await db.access_log.create({})
    count = await db.access_log.count()
    return PostCounterIncrementResponse(count=count)
