from langchain_chroma import Chroma

from src.embeddings import embeddings

vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory="chromadb/chromadb",
)