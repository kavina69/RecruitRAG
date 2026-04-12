from pathlib import Path
import fitz
from docx import Document


def extract_text_from_pdf(file_path: str) -> str:
    text = []
    doc = fitz.open(file_path)
    for page in doc:
        text.append(page.get_text())
    return "\n".join(text)


def extract_text_from_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_resume_text(file_path: str) -> str:
    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        return extract_text_from_pdf(file_path)
    elif suffix == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")