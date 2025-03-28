import sqlite3
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load text data from SQLite
def load_legal_docs():
    conn = sqlite3.connect("legal_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM legal_docs")
    data = cursor.fetchall()
    conn.close()
    return data

# Fetch stored legal documents
legal_docs = load_legal_docs()

# Extract document contents
doc_texts = [doc[2] for doc in legal_docs]

# Load pre-trained Sentence Transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Convert documents to embeddings
embeddings = model.encode(doc_texts, convert_to_numpy=True)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 similarity index
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "legal_faiss.index")

print("✅ FAISS Index created and saved successfully!")
