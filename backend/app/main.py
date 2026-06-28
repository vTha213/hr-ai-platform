from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine

from app.api.auth import router as auth_router
from app.api.jobs import router as jobs_router
from app.api.ai import router as ai_router
from app.api.resume import router as resume_router
from app.api.candidate import router as candidate_router
from app.api.screening import router as screening_router
from app.api.dashboard import router as dashboard_router
from app.api.social_media import router as social_media_router


app = FastAPI(
    title="HR AI Platform",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "HR AI Platform Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }


@app.get("/db-test")
async def db_test():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        value = result.scalar()

    return {
        "database": "connected",
        "value": value
    }


# Routers
app.include_router(auth_router)
app.include_router(jobs_router)
app.include_router(ai_router)
app.include_router(resume_router)
app.include_router(candidate_router)
app.include_router(screening_router)
app.include_router(dashboard_router)
app.include_router(social_media_router)