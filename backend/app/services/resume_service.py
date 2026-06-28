import os
import shutil
from uuid import uuid4

from fastapi import (
    HTTPException,
    UploadFile
)

UPLOAD_FOLDER = "uploads/resumes"

ALLOWED_TYPES = {
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
}

MAX_FILE_SIZE = 10 * 1024 * 1024


def save_resume(file: UploadFile):

    # -------------------------
    # MIME Validation
    # -------------------------
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )

    # -------------------------
    # File Size Validation
    # -------------------------
    file.file.seek(0, os.SEEK_END)
    size = file.file.tell()
    file.file.seek(0)

    if size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="Maximum file size is 10 MB."
        )

    # -------------------------
    # Extension Validation
    # -------------------------
    extension = file.filename.split(".")[-1].lower()

    if extension not in ["pdf", "docx"]:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )

    # -------------------------
    # Magic Byte Validation
    # -------------------------
    header = file.file.read(8)
    file.file.seek(0)

    if extension == "pdf":

        if not header.startswith(b"%PDF"):
            raise HTTPException(
                status_code=400,
                detail="Invalid PDF file."
            )

    elif extension == "docx":

        # DOCX files are ZIP archives
        if not header.startswith(b"PK\x03\x04"):
            raise HTTPException(
                status_code=400,
                detail="Invalid DOCX file."
            )

    # -------------------------
    # Save File
    # -------------------------
    os.makedirs(
        UPLOAD_FOLDER,
        exist_ok=True
    )

    filename = f"{uuid4()}.{extension}"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return filename, filepath