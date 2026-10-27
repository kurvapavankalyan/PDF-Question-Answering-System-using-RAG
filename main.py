from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.generator import generate_answer
from src.pdf_loader import load_pdf
from src.retriever import retrieve_documents
from src.texsplit import split_documents
from src.vector_store import vector_store


class Question(BaseModel):
    question: str


def prepare_documents():
    """Load the PDF and add its chunks to ChromaDB if the database is empty."""
    documents = load_pdf()
    chunks = split_documents(documents)

    if not chunks:
        raise RuntimeError("No text was found in the PDF.")

    if vector_store._collection.count() == 0:
        vector_store.add_documents(chunks)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Prepare the document once when the web server starts.
    prepare_documents()
    yield


app = FastAPI(title="RAG API", lifespan=lifespan)


@app.get("/health")
def health():
    """Check that the API is running."""
    return {"status": "ok"}


@app.post("/ask")
def ask(question: Question):
    """Find an answer in the PDF."""
    text = question.question.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Please enter a question.")

    documents = retrieve_documents(text)
    if not documents:
        return {"answer": "No relevant information found."}

    context = "\n\n".join(document.page_content for document in documents)
    answer = generate_answer(context, text)

    return {"answer": answer}
