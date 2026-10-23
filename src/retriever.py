from src.vector_store import vector_store


def retrieve_documents(question, k=2):
    return vector_store.similarity_search(query=question, k=k)