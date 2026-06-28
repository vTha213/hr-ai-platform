from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.user import User
from app.models.job import Job
from app.schemas.job import (
    JobCreate,
    JobUpdate,
    JobResponse
)
from app.core.security import get_current_user

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post(
    "",
    response_model=JobResponse
)
async def create_job(
    job: JobCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_job = Job(
        title=job.title,
        department=job.department,
        location=job.location,
        employment_type=job.employment_type,
        experience=job.experience,
        skills=job.skills,
        description=job.description,
        approved=False,
        created_by=current_user.id
    )

    db.add(new_job)
    await db.commit()
    await db.refresh(new_job)

    return new_job


@router.get(
    "",
    response_model=list[JobResponse]
)
async def get_jobs(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Job))
    return result.scalars().all()


@router.get(
    "/{job_id}",
    response_model=JobResponse
)
async def get_job(
    job_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Job).where(Job.id == job_id)
    )

    job = result.scalar_one_or_none()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job


@router.put(
    "/{job_id}",
    response_model=JobResponse
)
async def update_job(
    job_id: int,
    job_data: JobUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Job).where(Job.id == job_id)
    )

    job = result.scalar_one_or_none()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    job.title = job_data.title
    job.department = job_data.department
    job.location = job_data.location
    job.employment_type = job_data.employment_type
    job.experience = job_data.experience
    job.skills = job_data.skills
    job.description = job_data.description
    job.approved = job_data.approved

    await db.commit()
    await db.refresh(job)

    return job


@router.delete("/{job_id}")
async def delete_job(
    job_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Job).where(Job.id == job_id)
    )

    job = result.scalar_one_or_none()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    await db.delete(job)
    await db.commit()

    return {
        "message": "Job deleted successfully"
    }