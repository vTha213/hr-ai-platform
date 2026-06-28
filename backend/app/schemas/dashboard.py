from pydantic import BaseModel


class CandidateDashboardResponse(BaseModel):

    candidate_id: int
    name: str
    email: str
    job_title: str

    overall_score: int
    github_score: int

    recommendation: str
    screening_status: str

    class Config:
        from_attributes = True


class CandidateDetailResponse(BaseModel):

    candidate_id: int

    name: str
    email: str
    phone: str

    linkedin_url: str
    github_url: str

    job_title: str

    overall_score: int
    skills_score: int
    experience_score: int
    education_score: int

    github_score: int
    linkedin_score: int

    # Combined Score Breakdown
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

    class Config:
        from_attributes = True


class LinkedInReviewRequest(BaseModel):

    linkedin_score: int


class LinkedInReviewResponse(BaseModel):

    message: str

    linkedin_score: int