from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import os
import pdfplumber

def extract_text_from_pdfs(data_folder):
    all_texts = []
    found = False
    for file in os.listdir(data_folder):
        if file.endswith('.pdf'):
            found = True
            print(f"Reading {file}")
            pdf_path = os.path.join(data_folder, file)
            text = ''
            with pdfplumber.open(pdf_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    t = page.extract_text()
                    print(f"Page {i+1}: {'Has content' if t else 'EMPTY'}")
                    if t:
                        text += t + "\n"
            if text:
                print(f"File {file} - extracted {len(text)} characters with pdfplumber.")
                all_texts.append(text)
            else:
                print(f"File {file} appears empty.")
    if not found:
        print("No PDF files found in the data folder!")
    return all_texts

def split_texts(texts, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = []
    for txt in texts:
        chunks.extend(splitter.split_text(txt))
    return chunks

def main():
    # Data folder is in the parent directory
    data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
    texts = extract_text_from_pdfs(data_folder)
    print(f"Extracted texts from {len(texts)} PDF(s).")
    chunks = split_texts(texts)
    print(f"Split into {len(chunks)} chunks.")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    print(f"Embedded {len(embeddings)} chunks.")
    # Vector DB in the parent directory
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../vector_db/chroma_db'))
    chroma_client = chromadb.PersistentClient(path=db_path)
    collection = chroma_client.get_or_create_collection(name="safety")
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(ids=[f"chunk_{i}"], embeddings=[emb.tolist()], documents=[chunk])
    print(f"✅ Vector DB built and persisted to {db_path}")

if __name__ == "__main__":
    main()