from typing import NotRequired, TypedDict

from database import db
from fastapi import APIRouter
from prisma import Prisma
from prisma.models import AccessLog
from pydantic import BaseModel
from utils import cast_json_dict, encode_json

router = APIRouter()


class Metadata(TypedDict):
    dummy: NotRequired[int]


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
    metadata: Metadata = {"dummy": 123}
    await db.access_log.create(data={"metadata": encode_json(metadata)})
    count = await db.access_log.count()
    return PostCounterIncrementResponse(count=count)


@router.get("/access_log/latest")
async def get_access_log_latest() -> AccessLog:
    access_log = await db.access_log.find_first_or_raise(order={"request_time": "desc"})
    return access_log
