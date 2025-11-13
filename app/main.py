from fastapi import FastAPI

from app.lifespan import lifespan
from app.interfaces.rest.routers.electronic_board_router import router as boards_router

app = FastAPI(
    title="REMS Electric Panels API",
    version="1.0.0",
    description="API for managing electronic boards",
    lifespan=lifespan
)

app.include_router(boards_router)

@app.get("/health", tags=["Health"])
async def health():
    """
    Health check endpoint.
    """
    return {"status": "ok"}