def generate_match_explanation(query: str, retrieved_chunks: list):
    if not retrieved_chunks:
        return "No matching candidates were found for the given query."

    explanation = []
    explanation.append(f"Search Query: {query}")
    explanation.append("")
    explanation.append("Top Matching Resume Chunks:")
    explanation.append("")

    for i, chunk in enumerate(retrieved_chunks[:5], start=1):
        short_chunk = chunk[:300].replace("\n", " ")
        explanation.append(f"{i}. {short_chunk}...")

    explanation.append("")
    explanation.append(
        "These candidates were matched based on semantic similarity between the recruiter query and the resume content."
    )

    return "\n".join(explanation)