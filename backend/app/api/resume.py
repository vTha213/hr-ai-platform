from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.user import User
from app.models.resume import Resume
from app.schemas.resume import ResumeResponse
from app.core.security import get_current_user

from app.services.resume_service import save_resume
from app.services.resume_parser import extract_resume_text

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post(
    "/upload",
    response_model=ResumeResponse
)
async def upload_resume(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Save uploaded file
    filename, filepath = save_resume(file)

    # Extract text from PDF/DOCX
    resume_text = extract_resume_text(filepath)

    # Save to database
    resume = Resume(
        filename=filename,
        filepath=filepath,
        resume_text=resume_text,
        uploaded_by=current_user.id
    )

    db.add(resume)

    await db.commit()

    await db.refresh(resume)

    return resume