from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db

from app.schemas.screening import ScreeningResponse

from app.services.screening_service import run_screening


router = APIRouter(
    prefix="/screening",
    tags=["AI Screening"]
)


@router.post(
    "/{candidate_id}",
    response_model=ScreeningResponse
)
async def screening_candidate(
    candidate_id: int,
    db: AsyncSession = Depends(get_db)
):

    screening = await run_screening(
        candidate_id=candidate_id,
        db=db
    )

    if screening is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    return screening