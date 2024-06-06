from fastapi import APIRouter
from prisma import Prisma
from pydantic import BaseModel

router = APIRouter()

db = Prisma()


class GetCounterCountResponse(BaseModel):
    count: int


@router.get("/counter/count")
async def get_counter_count() -> GetCounterCountResponse:
    await db.connect()
    count = await db.accesslog.count()
    await db.disconnect()
    return GetCounterCountResponse(count=count)


class PostCounterIncrementResponse(BaseModel):
    count: int


@router.post("/counter/increment")
async def post_counter_increment() -> PostCounterIncrementResponse:
    await db.connect()
    await db.accesslog.create({})
    count = await db.accesslog.count()
    await db.disconnect()
    return PostCounterIncrementResponse(count=count)
