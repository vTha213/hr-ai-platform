from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.db.database import engine
from app.db.base import Base

# Import all models so SQLAlchemy knows about them
from app.models.user import User
from app.models.job import Job
from app.models.candidate import Candidate
from app.models.resume import Resume
from app.models.screening import Screening

from app.api.auth import router as auth_router
from app.api.jobs import router as jobs_router
from app.api.ai import router as ai_router
from app.api.resume import router as resume_router
from app.api.candidate import router as candidate_router
from app.api.screening import router as screening_router
from app.api.dashboard import router as dashboard_router
from app.api.social_media import router as social_media_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="HR AI Platform",
    version="1.0.0",
    description="AI Powered Recruitment Platform",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "HR AI Platform Running"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/db-test")
async def db_test():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        value = result.scalar()

    return {
        "database": "connected",
        "value": value,
    }


@app.get("/debug-db")
async def debug_db():
    return {
        "database_url": os.getenv("DATABASE_URL"),
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