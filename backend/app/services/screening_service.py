from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.candidate import Candidate
from app.models.resume import Resume
from app.models.job import Job
from app.models.screening import Screening

from app.services.ai_screening import screen_candidate
from app.services.github_service import get_github_profile
from app.services.github_ai import analyze_github
from app.services.resume_flag import detect_ai_resume


async def run_screening(
    candidate_id: int,
    db: AsyncSession
):

    # Candidate
    result = await db.execute(
        select(Candidate).where(
            Candidate.id == candidate_id
        )
    )

    candidate = result.scalar_one_or_none()

    if candidate is None:
        return None

    # Resume
    result = await db.execute(
        select(Resume).where(
            Resume.id == candidate.resume_id
        )
    )

    resume = result.scalar_one()

    # Job
    result = await db.execute(
        select(Job).where(
            Job.id == candidate.job_id
        )
    )

    job = result.scalar_one()

    # AI Resume Screening
    ai_result = screen_candidate(
        resume.resume_text,
        job.description
    )

    # GitHub Profile
    github_result = get_github_profile(
        candidate.github_url
    )

    # GitHub AI
    github_ai_result = analyze_github(
        github_result,
        resume.resume_text
    )

    # Resume AI Detection
    resume_flag = detect_ai_resume(
        resume.resume_text
    )

    # Existing Screening
    result = await db.execute(
        select(Screening).where(
            Screening.candidate_id == candidate.id
        )
    )

    screening = result.scalar_one_or_none()

    if screening is None:

        screening = Screening(

            candidate_id=candidate.id,

            overall_score=0,
            skills_score=0,
            experience_score=0,
            education_score=0,

            github_score=0,
            linkedin_score=0,

            cv_contribution=0,
            github_contribution=0,
            linkedin_contribution=0,
            final_score=0,

            github_summary="",

            ai_generated_probability=0,

            strengths="",
            weaknesses="",

            recommendation="",

            screening_status="Processing"

        )

        db.add(screening)

    # CV Scores
    screening.overall_score = ai_result["overall_score"]
    screening.skills_score = ai_result["skills_score"]
    screening.experience_score = ai_result["experience_score"]
    screening.education_score = ai_result["education_score"]

    # GitHub
    screening.github_score = github_ai_result["github_score"]
    screening.github_summary = github_ai_result["github_summary"]

    # AI Resume Flag
    screening.ai_generated_probability = (
        resume_flag["ai_generated_probability"]
    )

    # AI Reasoning
    screening.strengths = ai_result["strengths"]
    screening.weaknesses = ai_result["weaknesses"]
    screening.recommendation = ai_result["recommendation"]

    # Weighted Scores
    screening.cv_contribution = round(
        screening.overall_score * 0.70,
        2
    )

    screening.github_contribution = round(
        screening.github_score * 0.15,
        2
    )

    screening.linkedin_contribution = round(
        screening.linkedin_score * 0.15,
        2
    )

    screening.final_score = round(

        screening.cv_contribution
        + screening.github_contribution
        + screening.linkedin_contribution,

        2

    )

    screening.screening_status = "Completed"

    await db.commit()

    await db.refresh(screening)

    return screening