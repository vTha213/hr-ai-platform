import fitz
from docx import Document


def extract_pdf_text(filepath: str) -> str:
    text = ""

    pdf = fitz.open(filepath)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


def extract_docx_text(filepath: str) -> str:
    text = ""

    doc = Document(filepath)

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def extract_resume_text(filepath: str) -> str:

    if filepath.endswith(".pdf"):
        return extract_pdf_text(filepath)

    if filepath.endswith(".docx"):
        return extract_docx_text(filepath)

    raise Exception("Unsupported file format")