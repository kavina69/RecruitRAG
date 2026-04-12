import os
from fastapi import FastAPI, UploadFile, File
from app.parser import extract_resume_text
from app.chunker import chunk_text
from app.embedder import get_embedding
from app.endee_client import upsert_vector, create_collection
from app.retriever import search_candidates
from app.rag import generate_match_explanation

app = FastAPI()

UPLOAD_DIR = "data/resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.on_event("startup")
def startup_event():
    vector = get_embedding("test")
    create_collection(len(vector))


@app.get("/")
def home():
    return {"message": "RecruitRAG is running"}


@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_resume_text(file_path)
    chunks = chunk_text(text)

    for i, chunk in enumerate(chunks):
        vector = get_embedding(chunk)
        metadata = {
            "file_name": file.filename,
            "chunk_id": i
        }
        item_id = f"{file.filename}_{i}"
        upsert_vector(item_id, vector, chunk, metadata)

    return {
        "status": "success",
        "file": file.filename,
        "chunks_indexed": len(chunks)
    }


@app.get("/search")
def search(query: str, top_k: int = 5):
    results = search_candidates(query, top_k=top_k)

    chunks = []
    for r in results.get("results", []):
        if "text" in r:
            chunks.append(r["text"])

    explanation = generate_match_explanation(query, chunks)

    return {
        "query": query,
        "results": results,
        "rag_explanation": explanation
    }