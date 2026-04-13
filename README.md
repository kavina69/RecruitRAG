# RecruitRAG + RAG using Endee

RecruitRAG is a resume semantic search and candidate matching system built using FastAPI.

## Features
- Upload resumes in PDF/DOCX format
- Extract text from resumes
- Split resume text into chunks
- Search candidates using natural language query
- Return top matching results
- Generate explanation for candidate matching

## Tech Stack
- Python
- FastAPI
- PyMuPDF
- python-docx

## Endee Usage
This project is designed with a vector database layer similar to Endee.

Currently, the project uses an in-memory mock vector search implementation for local testing. The retrieval layer is modular and can be replaced with Endee for scalable production-level semantic search.

## Run the Project

```bash
python -m uvicorn app.main:app --reload