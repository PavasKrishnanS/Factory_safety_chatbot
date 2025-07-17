print("Importing chatbot.py...")

from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import requests

model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded OK.")

# IMPORTANT: Do *not* use get_or_create_collection, use get_collection for prod.
chroma_client = chromadb.PersistentClient(path="./vector_db/chroma_db")
collection = chroma_client.get_collection(name="safety")
print("Chroma collection loaded OK.")

def retrieve_context(user_query, top_k=8):
    user_emb = model.encode([user_query])[0]
    res = collection.query(query_embeddings=[user_emb.tolist()], n_results=top_k, include=['documents', 'distances'])
    docs = res["documents"][0]
    dists = res.get("distances", [[1]*top_k])[0]
    print("-----------")
    print("QUERY:", user_query)
    print("RETRIEVED DOCS AND DISTANCES:")
    for doc, dist in zip(docs, dists):
        print(f"- [{dist:.6f}] {doc[:500].replace(chr(10), ' ')}")
    print("-----------")

    # Filter out very bad matches (Cosine distance threshold, optional)
    THRESHOLD = 0.5
    relevant = [doc for doc, dist in zip(docs, dists) if dist < THRESHOLD]
    if not relevant:
        relevant = docs[:1]  # fallback: send top doc
    if not relevant or not "".join(relevant).strip():
        return ""
    # Optionally, you can join more than one relevant chunk if you wish:
    return "\n".join(relevant)

def ask_ollama(question, context):
  
    prompt = (
    "You are an AI assistant specializing in industrial safety. "
    "Answer ONLY based on the provided CONTEXT from the safety manual below. "
    "If you don't find an answer in the context, respond: "
    "'Sorry, I don't have enough information to answer this prompt.' "
    "Your answer should be as detailed and comprehensive as possible. "
    "Include as much relevant info and explanation as the context allows. "
    "Use multiple bullet points, numbered steps, or paragraphs if needed. "
    "Do NOT summarize into just 1 or 2 sentences—expand fully and deeply.\n\n"
    f"CONTEXT:\n{context}\n\n"
    f"QUESTION: {question}\n\n"
    f"ANSWER:"
)  




    data = {"model": "gemma3:latest", "prompt": prompt, "stream": False}
    response = requests.post("http://localhost:11434/api/generate", json=data)
    res = response.json()
    if "response" in res:
        return res["response"].strip()
    else:
        return f"GEMMA ERROR: Got response: {res}"

def get_answer(user_question):
    context = retrieve_context(user_question)
    if not context:
        return "Sorry, I don't have enough information to answer that about industrial safety."
    return ask_ollama(user_question, context)

if __name__ == "__main__":
    print("Chatbot ready. Type your question or 'quit'.")
    while True:
        q = input("> ")
        if q.lower() in ["quit", "exit"]:
            break
        print(get_answer(q))