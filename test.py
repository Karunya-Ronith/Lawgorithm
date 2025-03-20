import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text("text") + "\n\n"

    return full_text

ipc_text = extract_text_from_pdf("IPC.pdf")

from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
ipc_chunks = splitter.split_text(ipc_text)


from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document


# Load Embedding Model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Convert text chunks into Documents
ipc_docs = [Document(page_content=chunk) for chunk in ipc_chunks]

# Generate embeddings
ipc_vectors = embedding_model.embed_documents([doc.page_content for doc in ipc_docs])

# Create FAISS Index (Proper Syntax)
ipc_index = FAISS.from_documents(ipc_docs, embedding_model)

# Save index
ipc_index.save_local("legal_index")


def retrieve_relevant_text(query):
    query_embedding = embedding_model.embed_query(query)
    retrieved_docs = ipc_index.similarity_search(query_embedding, k=3)  # Retrieve top 3 results

    return "\n\n".join([doc.page_content for doc in retrieved_docs])


query = "What is the punishment for rape?"
retrieved_text = retrieve_relevant_text(query)
print(retrieved_text)
