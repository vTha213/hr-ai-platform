from app.db.database import AsyncSessionLocal
from app.services.screening_service import run_screening


async def run_screening_background(
    candidate_id: int
):
    async with AsyncSessionLocal() as db:
        await run_screening(
            candidate_id=candidate_id,
            db=db
        )