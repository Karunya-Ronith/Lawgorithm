import streamlit as st
import faiss
import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer
import requests
import torch

st.title("💬 Indian Legal Chatbot")

# Load the FAISS index and embedding model
index = faiss.read_index("legal_faiss.index")
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load legal documents from SQLite
def load_legal_docs():
    conn = sqlite3.connect("legal_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM legal_docs")
    data = cursor.fetchall()
    conn.close()
    return data

legal_docs = load_legal_docs()

# User input
user_query = st.text_input("Enter your legal question:")

if st.button("Ask"):
    if user_query:
        query_embedding = embed_model.encode([user_query])
        D, I = index.search(query_embedding, k=2)
        best_match_index = I[0][0]
        best_doc = legal_docs[best_match_index][2]

        prompt = f"""
            You are an Indian legal expert. Answer strictly based on the legal document:
            {best_doc}

            Q: {user_query}
            A:
        """
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False}
        ).json()

        st.subheader("Answer:")
        st.write(response.get("response", "Sorry, no answer generated."))
