from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db

from app.models.job import Job
from app.models.user import User

from app.schemas.social_media import SocialMediaResponse

from app.services.social_media_ai import (
    generate_social_media_posts
)

from app.core.security import get_current_user

router = APIRouter(
    prefix="/social-media",
    tags=["Social Media Assistant"]
)


@router.post(
    "/{job_id}",
    response_model=SocialMediaResponse
)
async def generate_social_media(
    job_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

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

    ai_result = generate_social_media_posts(
        job.title,
        job.description
    )

    return SocialMediaResponse(

        linkedin_post=ai_result["linkedin_post"],

        twitter_post=ai_result["twitter_post"],

        facebook_post=ai_result["facebook_post"],

        instagram_post=ai_result["instagram_post"],

        suggested_groups=ai_result["suggested_groups"],

        image_prompt=ai_result["image_prompt"]

    )

@router.get("/test-auth")
async def test_auth(
    current_user: User = Depends(get_current_user)
):
    return {
        "message": "Authentication Working",
        "email": current_user.email
    }