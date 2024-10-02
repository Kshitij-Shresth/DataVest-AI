#Function to handle all user queries
def ask_question(question):
    docs = vector_store.similarity_search(question, k=1)
    if not docs:
        return "I'm sorry, I couldn't find any relevant information to answer your question."
    context = " ".join([doc.page_content for doc in docs])
    response = qa_model(question=question, context=context)

    return response['answer']
