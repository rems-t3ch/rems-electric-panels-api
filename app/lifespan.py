from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.infrastructure.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan context manager.
    Initializes the database before the application starts.
    """
    await init_db()
    yield