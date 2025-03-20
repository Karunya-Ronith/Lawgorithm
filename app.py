import streamlit as st
import requests

st.title("⚖️ Free Indian Legal Chatbot")
st.write("Ask me any legal question related to Indian law!")

user_input = st.text_area("Enter your legal query:")

if st.button("Get Answer"):
    if user_input:
        response = requests.post("http://127.0.0.1:5000/query", json={"query": user_input})
        st.write(response.json()["response"])
    else:
        st.warning("Please enter a question.")
