import math
from collections import Counter


def get_embedding(text: str):
    text = text.lower().strip()

    if not text:
        return [0.0] * 26

    counts = Counter(c for c in text if c.isalpha())
    vector = [float(counts.get(chr(ord('a') + i), 0)) for i in range(26)]

    norm = math.sqrt(sum(x * x for x in vector))
    if norm == 0:
        return vector

    return [x / norm for x in vector]