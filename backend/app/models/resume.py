from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    DateTime
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.db.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    filename: Mapped[str] = mapped_column(
        String(255)
    )

    filepath: Mapped[str] = mapped_column(
        String(500)
    )

    resume_text: Mapped[str] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )