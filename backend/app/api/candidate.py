from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Form,
    HTTPException,
    BackgroundTasks
)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db

from app.models.job import Job
from app.models.resume import Resume
from app.models.candidate import Candidate
from app.models.screening import Screening

from app.services.resume_service import save_resume
from app.services.resume_parser import extract_resume_text
from app.services.background_screening import (
    run_screening_background
)

router = APIRouter(
    prefix="/apply",
    tags=["Candidate Application"]
)


@router.post("/{job_id}")
async def apply_job(

    background_tasks: BackgroundTasks,

    job_id: int,

    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),

    linkedin_url: str = Form(...),
    github_url: str = Form(""),

    consent_given: bool = Form(...),

    resume: UploadFile = File(...),

    db: AsyncSession = Depends(get_db)

):

    # Check Job
    result = await db.execute(
        select(Job).where(
            Job.id == job_id
        )
    )

    job = result.scalar_one_or_none()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    # Consent
    if not consent_given:
        raise HTTPException(
            status_code=400,
            detail="Consent is required."
        )

    # Save Resume
    filename, filepath = save_resume(resume)

    resume_text = extract_resume_text(filepath)

    resume_obj = Resume(
        filename=filename,
        filepath=filepath,
        resume_text=resume_text
    )

    db.add(resume_obj)

    await db.commit()

    await db.refresh(resume_obj)

    # Check Existing Candidate
    result = await db.execute(
        select(Candidate).where(
            Candidate.email == email
        )
    )

    candidate = result.scalar_one_or_none()

    # ===========================
    # Existing Candidate
    # ===========================
    if candidate:

        candidate.job_id = job_id
        candidate.resume_id = resume_obj.id
        candidate.name = name
        candidate.phone = phone
        candidate.linkedin_url = linkedin_url
        candidate.github_url = github_url
        candidate.consent_given = consent_given
        candidate.status = "Applied"

        # Reset Previous Screening
        result = await db.execute(
            select(Screening).where(
                Screening.candidate_id == candidate.id
            )
        )

        screening = result.scalar_one_or_none()

        if screening:

            screening.overall_score = 0
            screening.skills_score = 0
            screening.experience_score = 0
            screening.education_score = 0

            screening.github_score = 0
            screening.linkedin_score = 0

            screening.cv_contribution = 0
            screening.github_contribution = 0
            screening.linkedin_contribution = 0

            screening.final_score = 0

            screening.github_summary = ""

            screening.ai_generated_probability = 0

            screening.strengths = ""
            screening.weaknesses = ""
            screening.recommendation = ""

            screening.screening_status = "Processing"

        await db.commit()

        # Run AI Screening in Background
        background_tasks.add_task(
            run_screening_background,
            candidate.id
        )

        return {
            "message": "Application Updated",
            "candidate_id": candidate.id,
            "screening_status": "Processing"
        }

    # ===========================
    # New Candidate
    # ===========================

    candidate = Candidate(
        job_id=job_id,
        resume_id=resume_obj.id,
        name=name,
        email=email,
        phone=phone,
        linkedin_url=linkedin_url,
        github_url=github_url,
        consent_given=consent_given,
        status="Applied"
    )

    db.add(candidate)

    await db.commit()

    await db.refresh(candidate)

    # Run AI Screening in Background
    background_tasks.add_task(
        run_screening_background,
        candidate.id
    )

    return {
        "message": "Application Submitted",
        "candidate_id": candidate.id,
        "screening_status": "Processing"
    }