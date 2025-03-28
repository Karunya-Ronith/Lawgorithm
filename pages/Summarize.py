import streamlit as st
import fitz
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import sqlite3

st.title("📄 Upload & Summarize Legal Document")

tokenizer = AutoTokenizer.from_pretrained("patrickvonplaten/bert2bert_cnn_daily_mail")
model = AutoModelForSeq2SeqLM.from_pretrained("patrickvonplaten/bert2bert_cnn_daily_mail")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    def extract_text(file):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n\n".join(page.get_text("text") for page in doc)

    pdf_text = extract_text(uploaded_file)
    st.success("Text extracted successfully!")

    with st.spinner("Summarizing..."):
        inputs = tokenizer(pdf_text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = model.generate(inputs.input_ids, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    st.subheader("Summary:")
    st.write(summary)

    # Save to database
    conn = sqlite3.connect("legal_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO legal_docs (title, content) VALUES (?, ?)", (uploaded_file.name, pdf_text))
    conn.commit()
    conn.close()
    st.success("Document saved to database!")
