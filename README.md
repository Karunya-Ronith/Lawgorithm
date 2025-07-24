# Lawgorithm

Lawgorithm is an AI-powered legal assistant tailored for the Indian legal system. It provides instant legal insights, generates rental agreements, summarizes legal documents, and translates Hindi legal documents to English. The application is built with Streamlit and leverages advanced NLP models for document search and generation.

## Features

- **Legal Chatbot:** Get AI-powered answers to your legal questions based on Indian law.
- **Legal Document Summarization:** Upload PDFs and receive concise summaries.
- **Rental Agreement Generator:** Create legally valid rental agreements in minutes.
- **Hindi Legal Document Translation:** Upload Hindi legal documents and get accurate English translations.

## Directory Structure

```
.
├── App.py                        # Main Streamlit app (landing page)
├── pages/
│   ├── Chatbot.py                # Legal chatbot interface
│   ├── Rental_Agreement.py       # Rental agreement generator
│   └── Hindi_Tanslation.py       # Hindi to English document translator
├── Data/
│   ├── *.pdf                     # Legal documents (Banking Law, IPC, etc.)
├── Data Preparation/
│   ├── extract.py                # PDF text extraction and DB population
│   └── faiss_indexer.py          # Embedding and FAISS index creation
├── legal_data.db                 # SQLite database of legal documents
├── legal_faiss.index             # FAISS index for semantic search
├── Images/                       # Team member images
├── read_db.py                    # Script to read from the database
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## Setup Instructions (Windows)

### 1. Clone the Repository
```sh
git clone <repo-url>
cd Lawgorithm
```

### 2. Install Python Dependencies
Create a virtual environment (recommended):
```sh
python -m venv venv
venv\Scripts\activate
```
Install required packages:
```sh
pip install -r requirements.txt
```

> **Note:**
> - For OCR translation, [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) must be installed. On Windows, set the path in `pages/Hindi_Tanslation.py` (default: `C:/Program Files/Tesseract-OCR/tesseract.exe`).
> - Some features require [Ollama](https://ollama.com/) or a local LLM API running at `http://localhost:11434`.

### 3. Prepare the Data
- Place your legal PDFs in the `Data/` directory.
- Run the extraction and indexing scripts:

```sh
python "Data Preparation/extract.py"
python "Data Preparation/faiss_indexer.py"
```

### 4. Launch the App
```sh
streamlit run App.py
```

## Usage
- **Home:** Overview and team info.
- **Chatbot:** Ask legal questions (uses semantic search + LLM).
- **Rental Agreement:** Fill the form to generate a rental agreement and download as `.docx`.
- **Hindi Translation:** Upload an image with Hindi text to extract and translate to English, then download as `.docx`.

## Dependencies
All dependencies are listed in [`requirements.txt`](requirements.txt). Install them using:
```sh
pip install -r requirements.txt
```

## Data
The `Data/` folder contains legal PDFs (e.g., IPC, Company Law, Constitution, etc.) used for search and Q&A.

## Team
- L Karunya Ronith
- Manav M Bajaj
- Abhijeet Srivathsan

## Notes
- Designed and tested on Windows. Adjust file paths as needed for your environment.
- For any issues, ensure all dependencies are installed and the database/index files are generated.