from langchain_community.document_loaders import PyPDFLoader


def load_pdf():
    loader = PyPDFLoader("data/sample.pdf")
    return loader.load()
