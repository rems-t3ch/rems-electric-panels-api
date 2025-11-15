from fastapi import FastAPI

from app.lifespan import lifespan
from app.interfaces.rest.routers.electronic_panel_router import router as panels_router

app = FastAPI(
    title="REMS Electric Panels API",
    version="1.0.0",
    description="API for managing electronic panels",
    lifespan=lifespan
)

app.include_router(panels_router)

@app.get("/health", tags=["Health"])
async def health():
    """
    Health check endpoint.
    """
    return {"status": "ok"}