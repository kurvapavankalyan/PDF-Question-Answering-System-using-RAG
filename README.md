# RAG API

The FastAPI service loads the configured PDF into the existing ChromaDB store
when the application starts, then exposes a question-answering API.

## Run

From the `RAG` directory, install the dependencies and start the server:

```powershell
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Set `OPENAI_API_KEY` (or `OPENROUTER_API_KEY`) in the environment or in a
`.env` file in this directory before starting the service.

## Endpoints

- `GET /health` returns the service status.
- `POST /ask` accepts a JSON body such as `{"question": "What is this document about?"}`.
  The response contains only the `answer`.
- `GET /docs` provides the interactive OpenAPI documentation.

The FastAPI application is defined in `main.py`. `Question` describes the JSON
input, and the `/ask` route retrieves matching PDF text and returns an answer
without returning document metadata.
