from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    department: str
    location: str
    employment_type: str
    experience: str
    skills: str
    description: str


class JobUpdate(BaseModel):
    title: str
    department: str
    location: str
    employment_type: str
    experience: str
    skills: str
    description: str
    approved: bool


class JobResponse(JobCreate):
    id: int
    approved: bool

    class Config:
        from_attributes = True