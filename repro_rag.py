
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import sys

print("Phase 1: Loading model")
try:
    model = SentenceTransformer("all-MiniLM-l6-v2")
    print("Model loaded")
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(1)

print("Phase 2: Loading data")
try:
    with open("all_training_data.json","r",encoding="utf-8") as f:
        data = json.load(f)
    print(f"Data loaded: {len(data)} items")
except Exception as e:
    print(f"Error loading data: {e}")
    sys.exit(1)

print("Phase 3: Preparing documents")
document = []
try:
    for item in data:
        text =f"""
        {item["output"]}
        {item["input"]}
        """
        document.append(text)
    print(f"Documents prepared: {len(document)}")
except Exception as e:
    print(f"Error preparing docs: {e}")
    sys.exit(1)

print("Phase 4: Encoding")
try:
    embeddings = model.encode(document)
    print(f"Embeddings shape: {embeddings.shape}, dtype: {embeddings.dtype}")
except Exception as e:
    print(f"Error encoding: {e}")
    sys.exit(1)

print("Phase 5: Indexing")
try:
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    # The original code:
    index.add(np.array(embeddings))
    print("Index created/added")
except Exception as e:
    print(f"Error indexing: {e}")
    # Fix attempt log
    if "float32" in str(e):
        print("Suggest: ensure embeddings are float32")
    sys.exit(1)

print("Phase 6: Search Test")
try:
    query = "divorce"
    q_embedding = model.encode([query])
    _, idx = index.search(np.array(q_embedding), k=2)
    context = "\n\n".join([document[i] for i in idx[0]])
    print("Relevant context found")
except Exception as e:
    print(f"Error searching: {e}")
    sys.exit(1)

print("Success")
