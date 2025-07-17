import chromadb

chroma_client = chromadb.PersistentClient(path="./vector_db/chroma_db")
collection = chroma_client.get_collection(name="safety")

result = collection.get(include=["documents"])
docs = result["documents"]

matches = [doc for doc in docs if "weld" in doc.lower() or "ppe" in doc.lower()]
print(f"Found {len(matches)} chunk(s) with 'weld' or 'ppe':")
for i, doc in enumerate(matches):
    print(f"{i+1}. {doc[:400]}")