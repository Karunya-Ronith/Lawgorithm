import sqlite3
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text("text") + "\n\n"

    # Fix: Specify UTF-8 encoding for text file
    with open("demo.txt", "a", encoding="utf-8") as f:
        f.write(full_text)
    
    return full_text

# Extract text from the constitution PDF
pdf_text = extract_text_from_pdf("Banking Law.pdf")

# Store extracted text in SQLite
conn = sqlite3.connect("legal_data.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS legal_docs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
)
''')

# Fix: Handle potential encoding issues for SQLite
cursor.execute("INSERT INTO legal_docs (title, content) VALUES (?, ?)", 
               ("Banking Law", pdf_text))

conn.commit()
conn.close()

print("✅ Constitution PDF stored in SQLite successfully!")
