from typing import List, Dict, Any

DB = []


def create_collection(dim: int):
    return {"message": f"Mock collection created with dimension {dim}"}


def upsert_vector(item_id: str, vector: List[float], text: str, metadata: Dict[str, Any]):
    DB.append({
        "id": item_id,
        "vector": vector,
        "text": text,
        "metadata": metadata
    })
    return {"message": "stored"}


def cosine_similarity(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(y * y for y in b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def search_vectors(query_vector: List[float], top_k: int = 5):
    scored = []
    for item in DB:
        score = cosine_similarity(query_vector, item["vector"])
        scored.append({
            "score": score,
            "text": item["text"],
            "metadata": item["metadata"]
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return {"results": scored[:top_k]}