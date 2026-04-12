from app.embedder import get_embedding
from app.endee_client import search_vectors


def search_candidates(query: str, top_k: int = 5):
    query_vector = get_embedding(query)
    results = search_vectors(query_vector, top_k=top_k)
    return results