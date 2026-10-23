from pathlib import Path

from langchain_chroma import Chroma

from src.embeddings import embeddings

persist_directory = Path(__file__).resolve().parents[1] / "chromadb" / "chromadb"
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory=str(persist_directory),
)