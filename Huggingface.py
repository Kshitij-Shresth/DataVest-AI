#Initializing a vector store with FAISS
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
if not embeddings:
    raise ValueError("Embeddings could not be generated. Please check the embedding model.")

#FAISS vector store from the embedded documents
vector_store = FAISS.from_documents(texts, embeddings)
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
