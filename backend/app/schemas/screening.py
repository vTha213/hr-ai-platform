from datetime import datetime
from pydantic import BaseModel


class ScreeningResponse(BaseModel):

    id: int

    candidate_id: int

    overall_score: int
    skills_score: int
    experience_score: int
    education_score: int

    github_score: int
    linkedin_score: int

    cv_contribution: float
    github_contribution: float
    linkedin_contribution: float

    final_score: float

    github_summary: str

    ai_generated_probability: int

    strengths: str
    weaknesses: str

    recommendation: str

    screening_status: str

    created_at: datetime

    class Config:
        from_attributes = True