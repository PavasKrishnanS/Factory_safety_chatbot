# 🏭 Factory Safety Chatbot — AI-powered RAG System

<div align="center">
  <img src="https://img.shields.io/badge/AI-RAG-blue" alt="AI RAG Badge"/>
  <img src="https://img.shields.io/badge/Built_with-Ollama%2C%20Gemma3%2C%20ChromaDB%2C%20Streamlit-ff69b4" alt="Tech Stack"/>
</div>

A cutting-edge **Retrieval-Augmented Generation (RAG) chatbot** for industrial/factory safety.  
**Combines:** Local LLM (Gemma3 / Ollama), vector database (ChromaDB), semantic search, and modern UI.

**Why recruiters should care:**  
- End-to-end, production-grade RAG pipeline — not just LLMs, but document-grounded AI search.  
- Private, on-premise, and easily customizable.  
- Demonstrates full-stack AI and data engineering, not just code!

---

## 🚩 Why This Project?

> - AI for real industry: Serve instant, accurate, on-premises answers from your own safety manuals.
> - Modern RAG design: Embeddings, vector search, local document-constrained LLM.
> - Ready for confidential, critical use. No cloud APIs, no data leaks.

---

## 🧩 End-to-End RAG Pipeline (How this chatbot works)

### 1. Ingestion
- **Extract:** PDF(s) parsed into text with `pdfplumber`.
- **Split:** Text chunked (e.g., 500 char length/50 overlap) for precise retrieval.
- **Embed:** Each chunk encoded to a vector using `sentence-transformers` (`all-MiniLM-L6-v2`).
- **Store:** Stored into a persistent ChromaDB vector DB for high-speed semantic search.

### 2. Retrieval
- User asks a question in the chat UI.
- Question embedded to vector.
- ChromaDB does semantic similarity search, retrieving top-k most relevant chunks from manuals.

### 3. Augmentation (the “A” in RAG)
- Question and retrieved manual context passed together to Gemma3 LLM (running locally via Ollama).
- LLM generates **document-grounded answers** — no guessing/hallucination; only from your actual docs.
- If there’s no answer: "Sorry, I don’t have that information."

### 4. Serving
- [Streamlit](https://streamlit.io/) web interface: anyone in the factory can chat and ask safety questions, any time.

---

## ⚙️ Architecture Diagram

```mermaid
flowchart TD
    A[PDF Document(s)] --> B[Ingestion (pdfplumber, chunking)]
    B --> C[Embedding (SentenceTransformers)]
    C --> D[ChromaDB Vector Store]
    E[User Question] --> F[Embedding (SentenceTransformers)]
    F --> G[Similarity Search (ChromaDB)]
    D -- Top-K Chunks --> G
    G --> H[LLM via Ollama / Gemma3]
    H --> I[Answer shown in Streamlit UI]
📦 Setup & Usage
Prerequisites
Python 3.8+
Ollama (local): Download Ollama
Gemma3 model:
sh
Copy code
ollama pull gemma3
(Optional: Use a GPU with Ollama for better speed)
Installation
sh
Copy code
git clone https://github.com/YOURUSERNAME/factory-safety-chatbot.git
cd factory-safety-chatbot
python -m venv .venv
# Activate venv: (Windows:)
.venv\Scripts\activate
# (Mac/Linux:)
source .venv/bin/activate
pip install -r requirements.txt
Add Your Safety Documents
Place your PDF(s) in the data/ folder.
Ingest Documents into the DB
sh
Copy code
python app/ingest.py
Launch the Chatbot UI
sh
Copy code
streamlit run app/ui.py
The app is available at: http://localhost:8501

📁 Project Structure
graphql
Copy code
factory-safety-chatbot/
├── app/
│   ├── chatbot.py        # RAG backend orchestration
│   ├── ingest.py         # PDF > Chunk > Embeddings > ChromaDB
│   └── ui.py             # Streamlit web interface
├── data/                 # Place PDF safety manuals here
├── vector_db/            # ChromaDB persistent storage
├── inspect_db.py         # Inspect vector DB/debug tools
├── requirements.txt
└── README.md
💡 Example Use Cases
"What PPE is required for welding in our factory?"
"Explain lockout/tagout procedures."
"What’s our protocol for chemical spills?"
"Describe our emergency evacuation steps."
Empowers workers to get compliant, company-approved safety info in seconds!

🌟 Why This Demo Stands Out (For Recruiters)
True Retrieval-Augmented Generation:
Shows advanced grasp of vector search, semantic embeddings, prompt engineering.
Private by Default:
Runs on local hardware, no data leaves your facility.
Modular:
Easily swap in different LLMs (Mistral, Llama, etc.), add more docs, adjust chunking/embedding strategies.
Enterprise-Ready Pipeline:
Ingest, semantic search, RAG, and UI—all production-grade and auditable.
📝 License
MIT (for educational/demo purposes only; do not upload confidential or regulated documents to public repositories).

👋 Contact
Want to collaborate, see a live demo, or discuss deployment?

[Your LinkedIn] | [Your Email]

💼 Recruiter note:

This repo demonstrates my ability to design, implement, and explain full-scale AI RAG solutions for sensitive industry data—and to build privacy-first, document-grounded AI systems for real business impact.
