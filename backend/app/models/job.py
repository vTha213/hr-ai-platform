from sqlalchemy import String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(255)
    )

    department: Mapped[str] = mapped_column(
        String(255)
    )

    location: Mapped[str] = mapped_column(
        String(255)
    )

    employment_type: Mapped[str] = mapped_column(
        String(100)
    )

    experience: Mapped[str] = mapped_column(
        String(100)
    )

    skills: Mapped[str] = mapped_column(
        Text
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    approved: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )