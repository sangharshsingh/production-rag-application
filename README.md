# DocuMind — AI-Powered PDF Question Answering

DocuMind is a full-stack Retrieval-Augmented Generation (RAG) application that allows users to ask questions about an indexed PDF document and receive context-grounded answers.

The application combines semantic search, a persistent vector database, and a large language model to generate answers based on retrieved document content.

## Features

- AI-powered PDF question answering
- Semantic search using Hugging Face embeddings
- Persistent vector storage with ChromaDB
- LLM-powered answer generation using Groq
- REST API built with FastAPI
- Interactive chat interface built with Streamlit
- Retrieval evaluation using Precision@K, Recall@K, Hit Rate@K, and MRR
- Comparison of similarity search, MMR, multi-query retrieval, and Reciprocal Rank Fusion

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Frontend | Streamlit |
| Backend | FastAPI |
| LLM provider | Groq |
| LLM | openai/gpt-oss-20b |
| RAG orchestration | LangChain |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Vector database | ChromaDB |
| API server | Uvicorn |

## Architecture

```text
User
  |
  v
Streamlit Frontend
  |
  | HTTP POST /api/v1/chat
  v
FastAPI Backend
  |
  v
RAG Pipeline
  |
  +--> ChromaDB --> Relevant PDF Chunks
  |
  +--> Groq LLM --> Generated Answer
  |
  v
JSON Response
  |
  v
Streamlit Chat Interface
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the placeholders with the actual GitHub repository details.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and add your Groq API key.

### 5. Prepare the document database

Place a PDF at `data/sample.pdf` and run the project's document ingestion process to create the ChromaDB collection.

The sample PDF and generated vector database are not included in the repository.

### 6. Start the backend

```bash
python -m uvicorn api:app --reload
```

FastAPI documentation is available at `http://127.0.0.1:8000/docs`.

### 7. Start the frontend

In another terminal:

```bash
python -m streamlit run streamlit_app.py
```

Open `http://localhost:8501`.

## Retrieval Evaluation

The project includes experiments comparing four retrieval strategies:

| Strategy | Recall@5 | MRR@5 |
|---|---:|---:|
| Similarity | 0.806 | 0.650 |
| MMR | 0.722 | 0.681 |
| Multi-query | 0.722 | 0.617 |
| RRF | 0.806 | 0.650 |

These results are from a small six-question evaluation set using provisional page-level relevance labels. They are exploratory results, not a validated production benchmark.

## Future Improvements

- PDF upload and ingestion through the frontend
- Structured source citations
- Conversation-aware retrieval
- Automated evaluation
- Docker deployment
- CI/CD integration

## Project Purpose

This project was built to understand and implement an end-to-end RAG workflow, from PDF processing and vector retrieval to LLM integration, API development, and frontend interaction.
