import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_match_explanation(query: str, retrieved_chunks: list):
    context = "\n\n".join(
        [f"Candidate chunk {i + 1}:\n{chunk}" for i, chunk in enumerate(retrieved_chunks)]
    )

    prompt = f"""
You are a recruiter assistant.

Job Query:
{query}

Retrieved Resume Chunks:
{context}

Task:
1. Identify the top matching candidates
2. Explain why they match
3. Mention relevant skills, experience, and possible missing skills
4. Keep the answer concise and grounded only in the provided resume chunks
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful recruiter assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content