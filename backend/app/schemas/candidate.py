from datetime import datetime
from pydantic import BaseModel, EmailStr, HttpUrl


class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    linkedin_url: HttpUrl
    github_url: HttpUrl | None = None
    consent_given: bool


class CandidateResponse(BaseModel):
    id: int
    job_id: int
    resume_id: int

    name: str
    email: EmailStr
    phone: str

    linkedin_url: str
    github_url: str | None = None

    consent_given: bool
    status: str

    created_at: datetime

    class Config:
        from_attributes = True