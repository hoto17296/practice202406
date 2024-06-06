from os import getenv
from fastapi import FastAPI
import asyncpg

app = FastAPI()

@app.get("/counter")
async def get_counter():
    conn = await asyncpg.connect(getenv("DATABASE_URL"))
    await conn.execute("INSERT INTO access_log DEFAULT VALUES")
    count = await conn.fetchval("SELECT COUNT(1) FROM access_log")
    conn.close()
    return {"count": count}