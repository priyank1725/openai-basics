import os
import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv
from textblob import TextBlob

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Example sentences
sentences = [
    "I love programming in Python!",
    "This code is terrible and frustrating.",
    "The cat is sleeping on the sofa."
]

# Function to create hybrid embeddings
def create_hybrid_embedding(text):
    # --- AI Embedding from Gemini ---
    ai_embedding = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document"
    )["embedding"]

    # --- Custom Features ---
    sentiment = TextBlob(text).sentiment.polarity   # range: -1 (neg) → +1 (pos)
    length = len(text.split())                      # word count
    exclamation = 1 if "!" in text else 0           # exclamation mark present?

    print(np.array([sentiment, length, exclamation]))
    # --- Combine ---
    hybrid_vector = np.concatenate([
        np.array(ai_embedding),           # AI embedding
        np.array([sentiment, length, exclamation]) # Custom features
    ])

    return hybrid_vector

# Generate embeddings
hybrid_embeddings = [create_hybrid_embedding(s) for s in sentences]

# Check dimensions
print(f"Hybrid vector length: {len(hybrid_embeddings[0])}")

# Compare similarities (cosine)
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        sim = cosine_similarity(hybrid_embeddings[i], hybrid_embeddings[j])
        print(f"Similarity:\n  '{sentences[i]}'\n  '{sentences[j]}'\n  → {sim:.4f}\n")
