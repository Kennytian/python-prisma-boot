from typing import Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel

from src.config.prisma_config import connect_db, disconnect_db
from src.routers.product_routers import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await connect_db()
        yield
    finally:
        await disconnect_db()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"data": "Hello world from Python 👩‍❤️‍💋‍👨"}


app.include_router(product_router)
