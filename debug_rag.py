
import sys
import json

print("Checking imports...")
try:
    import numpy as np
    print("numpy imported")
except ImportError as e:
    print(f"ERROR importing numpy: {e}")

try:
    import faiss
    print("faiss imported")
except ImportError as e:
    print(f"ERROR importing faiss: {e}")
except Exception as e:
    print(f"ERROR importing faiss (runtime): {e}")

try:
    from sentence_transformers import SentenceTransformer
    print("sentence_transformers imported")
    print("Loading model...")
    model = SentenceTransformer("all-MiniLM-l6-v2")
    print("Model loaded.")
    test_emb = model.encode(["test"])
    print(f"Test encoding shape: {test_emb.shape}")
    print(f"Test encoding dtype: {test_emb.dtype}")

    import faiss
    import numpy as np
    
    print("Testing Faiss index creation...")
    dim = test_emb.shape[1]
    index = faiss.IndexFlatL2(dim)
    
    # Simulate the main code's insertion
    # In main code: index.add(np.array(embeddings))
    dummy_data = test_emb
    
    print(f"Adding data of dtype {dummy_data.dtype} to index...")
    try:
        index.add(dummy_data)
        print("Faiss add successful (direct)")
    except Exception as e:
        print(f"Faiss add failed (direct): {e}")
        
    # Check if conversion to float32 fixes it if it failed or just for info
    if dummy_data.dtype != np.float32:
        print("Attempting with explicit float32 cast...")
        try:
            index.add(dummy_data.astype(np.float32))
            print("Faiss add successful (with float32 cast)")
        except Exception as e:
            print(f"Faiss add failed (with float32 cast): {e}")

except ImportError as e:
    print(f"ERROR importing sentence_transformers: {e}")
except Exception as e:
    print(f"ERROR loading/using model: {e}")

print("Checking data...")
try:
    with open("all_training_data.json","r",encoding="utf-8") as f:
        data = json.load(f)
    print(f"Loaded {len(data)} items")
    for i, item in enumerate(data):
        if "input" not in item:
            print(f"ERROR: Missing 'input' key in item index {i}")
        if "output" not in item:
            print(f"ERROR: Missing 'output' key in item index {i}")
except FileNotFoundError:
    print("ERROR: all_training_data.json not found")
except json.JSONDecodeError as e:
    print(f"ERROR: JSON decode error: {e}")
except Exception as e:
    print(f"ERROR reading data: {e}")

print("Debug check complete.")
