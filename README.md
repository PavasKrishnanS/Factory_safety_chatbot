# 🏭 Factory Safety Chatbot — AI-Powered RAG with Small Language Model

[![AI-RAG](https://img.shields.io/badge/AI-RAG-blue)](#architecture)
[![Tech Stack](https://img.shields.io/badge/Stack-Ollama%20%7C%20Gemma3%20%7C%20ChromaDB%20%7C%20Streamlit-ff69b4)](#tech-stack)

---

**Factory Safety Chatbot** is a cutting-edge, Retrieval-Augmented Generation (RAG) system for answering factory/industrial safety questions—with local deployment and document-grounded answers.  
It combines a *Small Language Model* (Gemma 3 latest, via [Ollama](https://ollama.com/)), vector search ([ChromaDB](https://www.trychroma.com/)), and a Streamlit web app.  
       **This project proves real-world AI engineering + privacy best-practices (no big cloud LLMs!)**

---

## 🚩 Why This Project?

- **Real-World Impact:** Quickly answer vital safety questions from our *own* factory manuals.
- **Modern & Private:** No cloud. All LLM/RAG runs locally, perfect for confidential data.
- **Recruiter Appeal:** Full-stack AI: PDF → chunks → embedding → retrieval → LLM → web UI.

---

## 🧠 End-to-End RAG Pipeline

**1. Ingestion:**  
- PDFs are parsed with `pdfplumber`, split into overlapping “chunks.”
- Each chunk is embedded with [SentenceTransformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`).
- Embeddings & chunks are stored in a persistent [ChromaDB](https://www.trychroma.com/) vector DB.

**2. Retrieval:**  
- User’s question embedded and compared with your manual’s chunks.
- System retrieves the most semantically-similar text snippets.

**3. Augmentation (The "A" in RAG):**  
- The question and top-k document chunks are *sent to the LLM (Gemma 3B)*.
- The LLM is prompted to answer **strictly from your documentation context.**
- If answer isn't possible: `"Sorry, I don’t have that information."`

**4. Serving:**  
- Clean, modern web UI for chats, built with Streamlit.

---

## 🚀 Features

- **Private & secure:** Uses local LLM (Ollama with Gemma3) — no cloud API required!
- **Retrieval-Augmented Generation (RAG):** Answers only from your uploaded safety documents (factory manuals, procedures, etc).
- **Instant answers to safety questions:** PPE, chemical spills, lockout/tagout, evacuation, and more.
- **Easy web interface:** via Streamlit.

## 🛠️ Tech Stack

- **LLM:** [Ollama](https://ollama.com/) running `gemma3:latest` locally
- **Vector database:** ChromaDB (persistent, on-disk)
- **Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`)
- **PDF parsing:** pdfplumber
- **Frontend:** Streamlit
  

## 📦 Setup Instructions

**Prerequisites:**  
- Python 3.8+  
- Ollama installed & running locally (`ollama serve`)
- Download the Gemma3 model:  
  ```sh
  ollama pull gemma3
