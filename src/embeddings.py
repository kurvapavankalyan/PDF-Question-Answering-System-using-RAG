from langchain_openai import OpenAIEmbeddings

from src.generator import api_key, base_url

embeddings = OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    base_url=base_url,
    api_key=api_key,
)

print("embedding execution done!")