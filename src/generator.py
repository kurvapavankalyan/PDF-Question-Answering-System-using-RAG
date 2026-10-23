import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from src.prompt import prompt

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

api_key = (
    os.getenv("OPENAI_API_KEY")
    or os.getenv("OPENROUTER_API_KEY")
    or os.getenv("openai_api_key")
)
if not api_key:
    raise RuntimeError(
        "Missing API key. Set OPENAI_API_KEY, OPENROUTER_API_KEY, or "
        "openai_api_key in RAG/.env or your environment."
    )

base_url = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")

llm = ChatOpenAI(
    model="openai/gpt-4.1-mini",
    api_key=api_key,
    base_url=base_url,
    temperature=0,
    max_tokens=1024,
)

chain = prompt | llm


def generate_answer(context, question):
    response = chain.invoke({
        "context": context,
        "question": question
    })
    return response.content
