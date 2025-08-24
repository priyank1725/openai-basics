import os
import google.generativeai as genai # type: ignore
import numpy as np
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Sentences to compare
sentences = [
    "The cat is sleeping on the sofa",
    "A dog is resting on the couch",
    "I love programming in Python",
]

# Create embeddings
embeddings = []
for s in sentences:
    emb = genai.embed_content(
        model="models/embedding-001",
        content=s,
        task_type="retrieval_document"
    )
    embeddings.append(np.array(emb['embedding']))

# Cosine similarity function
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Compare first sentence with others
for i in range(0, len(sentences)):
    sim = cosine_similarity(embeddings[0], embeddings[i])
    print(f"Similarity between:\n  '{sentences[0]}'\n  '{sentences[i]}'\n  → {sim:.4f}\n")
