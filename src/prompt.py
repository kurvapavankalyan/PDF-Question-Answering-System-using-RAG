from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant that answers questions using the provided PDF context.

Context:
{context}

Question:
{question}

Instructions:
- Answer using only the provided context.
- If the answer is not available in the context, say:
  "I could not find the answer in the provided document."
- Do not make up information.
- Give a clear and concise answer.
""")