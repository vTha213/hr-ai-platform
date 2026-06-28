import asyncio

from app.db.base import Base
from app.db.database import engine

# Import models
from app.models.user import User
from app.models.job import Job
from app.models.resume import Resume
from app.models.candidate import Candidate
from app.models.screening import Screening


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )


if __name__ == "__main__":
    asyncio.run(create_tables())