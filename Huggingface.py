#Initializing a vector store with FAISS
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
if not embeddings:
    raise ValueError("Embeddings could not be generated. Please check the embedding model.")
