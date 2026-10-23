
from src.pdf_loader import load_pdf
from src.texsplit import split_documents
from src.vector_store import vector_store
from src.retriever import retrieve_documents
from src.generator import generate_answer


def main():
    documents = load_pdf()
    print(f"Loaded {len(documents)} pages from PDF.")

    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    if not chunks:
        print("No text was extracted from the PDF.")
        return

    if vector_store._collection.count() == 0:
        vector_store.add_documents(chunks)
        print("PDF chunks stored in ChromaDB.")
    else:
        print("Using existing ChromaDB data.")

    while True:
        try:
            question = input("\nEnter your question (or type 'exit'): ")
        except EOFError:
            print("\nGoodbye!")
            break

        if question.strip().lower() == "exit":
            print("Goodbye!")
            break

        if not question.strip():
            print("Please enter a question.")
            continue

        retrieved_docs = retrieve_documents(question)

        if not retrieved_docs:
            print("No relevant information found.")
            continue

        context = "\n\n".join(doc.page_content for doc in retrieved_docs)

        answer = generate_answer(context, question)

        print("\nAnswer:")
        print(answer)


if __name__ == "__main__":
    main()
