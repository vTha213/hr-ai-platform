from pydantic import BaseModel


# -------------------------
# Job Description Generator
# -------------------------

class JobDescriptionRequest(BaseModel):
    title: str
    experience: str
    skills: str


class JobDescriptionResponse(BaseModel):
    job_description: str


# -------------------------
# Resume Screening
# -------------------------

class ResumeScreenRequest(BaseModel):
    resume_id: int
    job_id: int


class ResumeScreenResponse(BaseModel):
    result: str