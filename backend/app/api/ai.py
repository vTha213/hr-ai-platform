from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db

from app.models.user import User
from app.models.job import Job
from app.models.resume import Resume

from app.core.security import get_current_user

from app.schemas.ai import (
    JobDescriptionRequest,
    JobDescriptionResponse,
    ResumeScreenRequest,
    ResumeScreenResponse
)

from app.services.ai_job_description import (
    generate_job_description,
    screen_resume
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post(
    "/generate-job-description",
    response_model=JobDescriptionResponse
)
async def ai_job_description(
    request: JobDescriptionRequest,
    current_user: User = Depends(get_current_user)
):

    job_description = generate_job_description(
        title=request.title,
        experience=request.experience,
        skills=request.skills
    )

    return {
        "job_description": job_description
    }


@router.post(
    "/screen-resume",
    response_model=ResumeScreenResponse
)
async def ai_resume_screening(
    request: ResumeScreenRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Get Resume
    resume_result = await db.execute(
        select(Resume).where(
            Resume.id == request.resume_id
        )
    )

    resume = resume_result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    # Get Job
    job_result = await db.execute(
        select(Job).where(
            Job.id == request.job_id
        )
    )

    job = job_result.scalar_one_or_none()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    result = screen_resume(
        resume_text=resume.resume_text,
        job_description=job.description
    )

    return {
        "result": result
    }