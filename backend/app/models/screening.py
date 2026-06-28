from datetime import datetime

from sqlalchemy import (
    Integer,
    Float,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.db.base import Base


class Screening(Base):
    __tablename__ = "screenings"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("candidates.id"),
        unique=True,
        nullable=False
    )

    overall_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    skills_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    experience_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    education_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    github_score: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    linkedin_score: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    cv_contribution: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    github_contribution: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    linkedin_contribution: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    final_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    github_summary: Mapped[str] = mapped_column(
        Text,
        default="",
        nullable=False
    )

    ai_generated_probability: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    strengths: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    weaknesses: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    recommendation: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    screening_status: Mapped[str] = mapped_column(
        Text,
        default="Completed",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )