import streamlit as st
import faiss
import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer
import requests
import torch

torch.classes.__path__ = [] # add this line to manually set it to empty.

# Load the FAISS index
index = faiss.read_index("legal_faiss.index")

# Load the embedding model
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

# Streamlit UI
st.title("⚖️ Lawgarithm Chatbot (India)")
st.write("Ask a legal question, and I will answer using relevant legal documents.")

# User input
user_query = st.text_input("Enter your legal question:")

if st.button("Ask"):
    if user_query:
        # Convert query to embedding
        query_embedding = embed_model.encode([user_query])
        
        # Search FAISS for the closest match
        D, I = index.search(query_embedding, k=2)  # Top 2 match
        best_match_index = I[0][0]

        # Retrieve the best matching legal document
        best_doc = legal_docs[best_match_index][2]  # Get content

        # Generate an answer using Ollama
        prompt = f"""
                    You are a highly knowledgeable Indian legal expert. 
                    Your task is to provide precise and professional responses strictly based on legal principles and the provided legal document.
                    Maintain a formal and objective tone.
                    Answer every question from a legal perspective.
                    If the question is not related to law, tell the user to ask a law related question.
                    Do not speculate or provide opinions.
                    Legal Document: 
                    {best_doc}

                    Q: {user_query}
                    A:
                """

        ollama_response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False}
        ).json()

        answer = ollama_response.get("response", "Sorry, I couldn't generate an answer.")

        # Display result
        st.subheader("Answer:")
        st.write(answer)

