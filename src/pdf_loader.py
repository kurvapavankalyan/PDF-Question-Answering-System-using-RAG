from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf():
    path = Path(__file__).resolve().parents[1] / "data" / "sample.pdf"
    loader = PyPDFLoader(str(path))
    return loader.load()
