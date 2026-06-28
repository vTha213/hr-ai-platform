from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db

from app.models.candidate import Candidate
from app.models.job import Job
from app.models.screening import Screening

from app.schemas.dashboard import (
    CandidateDashboardResponse,
    CandidateDetailResponse,
    LinkedInReviewRequest,
    LinkedInReviewResponse
)

router = APIRouter(
    prefix="/dashboard",
    tags=["HR Dashboard"]
)


# Candidate List
@router.get(
    "/candidates",
    response_model=list[CandidateDashboardResponse]
)
async def get_candidates(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(
            Candidate,
            Job,
            Screening
        )
        .join(
            Job,
            Candidate.job_id == Job.id
        )
        .join(
            Screening,
            Candidate.id == Screening.candidate_id
        )
    )

    rows = result.all()

    candidates = []

    for candidate, job, screening in rows:

        candidates.append(

            CandidateDashboardResponse(

                candidate_id=candidate.id,

                name=candidate.name,

                email=candidate.email,

                job_title=job.title,

                overall_score=screening.overall_score,

                github_score=screening.github_score,

                recommendation=screening.recommendation,

                screening_status=screening.screening_status

            )

        )

    return candidates


# Candidate Detail
@router.get(
    "/candidate/{candidate_id}",
    response_model=CandidateDetailResponse
)
async def get_candidate_detail(
    candidate_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(

        select(
            Candidate,
            Job,
            Screening
        )
        .join(
            Job,
            Candidate.job_id == Job.id
        )
        .join(
            Screening,
            Candidate.id == Screening.candidate_id
        )
        .where(
            Candidate.id == candidate_id
        )

    )

    row = result.first()

    if row is None:

        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    candidate, job, screening = row

    return CandidateDetailResponse(

        candidate_id=candidate.id,

        name=candidate.name,

        email=candidate.email,

        phone=candidate.phone,

        linkedin_url=candidate.linkedin_url,

        github_url=candidate.github_url,

        job_title=job.title,

        overall_score=screening.overall_score,

        skills_score=screening.skills_score,

        experience_score=screening.experience_score,

        education_score=screening.education_score,

        github_score=screening.github_score,

        linkedin_score=screening.linkedin_score,

        cv_contribution=screening.cv_contribution,

        github_contribution=screening.github_contribution,

        linkedin_contribution=screening.linkedin_contribution,

        final_score=screening.final_score,

        github_summary=screening.github_summary,

        ai_generated_probability=screening.ai_generated_probability,

        strengths=screening.strengths,

        weaknesses=screening.weaknesses,

        recommendation=screening.recommendation,

        screening_status=screening.screening_status

    )


# LinkedIn Manual Review
@router.patch(
    "/linkedin-review/{candidate_id}",
    response_model=LinkedInReviewResponse
)
async def update_linkedin_review(
    candidate_id: int,
    request: LinkedInReviewRequest,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Screening).where(
            Screening.candidate_id == candidate_id
        )
    )

    screening = result.scalar_one_or_none()

    if screening is None:
        raise HTTPException(
            status_code=404,
            detail="Screening not found"
        )

    if request.linkedin_score < 0 or request.linkedin_score > 100:
        raise HTTPException(
            status_code=400,
            detail="LinkedIn score must be between 0 and 100."
        )

    screening.linkedin_score = request.linkedin_score

    # Combined Score Calculation
    cv = screening.overall_score * 0.70
    github = screening.github_score * 0.15
    linkedin = request.linkedin_score * 0.15

    screening.cv_contribution = round(cv, 2)
    screening.github_contribution = round(github, 2)
    screening.linkedin_contribution = round(linkedin, 2)

    screening.final_score = round(
        cv + github + linkedin,
        2
    )

    await db.commit()

    await db.refresh(screening)

    return LinkedInReviewResponse(
        message="LinkedIn score updated successfully",
        linkedin_score=screening.linkedin_score
    )