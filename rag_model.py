
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# 1️⃣ Load model (ye hi "brain" hai)
print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2️⃣ JSON data load karo (Change: laws.json -> all_training_data.json)
print("Loading data...")
try:
    with open("all_training_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'all_training_data.json' nahi mili. Please file name check karein.")
    exit()

# 3️⃣ Text documents banao (RAG-friendly)
documents = []
for item in data:
    text = f"""
    {item.get('input', '')}
    {item.get('output', '')}
    """
    documents.append(text)

# 4️⃣ Embeddings banao (memory ban rahi hai)
print("Encoding data (thoda time lagega)...")
embeddings = model.encode(documents, show_progress_bar=True)

# 5️⃣ Vector store (FAISS)
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
# Fix: Ensure float32 for Faiss compatibility
index.add(np.array(embeddings).astype('float32'))

print("✅ RAG memory ready")

# 6️⃣ User se question lo
while True:
    query = input("\n❓ Question pucho (exit likho band karne ke liye): ")
    if query.lower().strip() == "exit":
        break
    if not query.strip():
        continue

    # 7️⃣ Question embedding
    q_embedding = model.encode([query])

    # 8️⃣ Relevant law nikaalo
    # Fix: Ensure float32 for Faiss search
    _, idx = index.search(np.array(q_embedding).astype('float32'), k=2)
    context = "\n\n".join([documents[i] for i in idx[0]])

    # 9️⃣ Simple answer (abhi LLM nahi, sirf context show)
    print("\n📌 Relevant Law:")
    print(context)
