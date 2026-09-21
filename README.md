# RAGChain

A modular Retrieval-Augmented Generation (RAG) framework built with LangChain, designed for flexible document ingestion, embedding, and semantic search.

## Overview

RAGChain provides a clean architecture for building RAG pipelines with swappable embedding models, persistent vector storage, and a config-driven approach to model management.

## Architecture

```
Ingestion ───▶  Embedding Layer   Vector Store 
Pipeline        (Config-Driven)    (ChromaDB)  
                     │                 │
                     ▼                 ▼
                   Registry      Retriever  
                   & Router      (Search)   
                            
```

## Features

- **Pluggable Embedding Models** — Switch between HuggingFace and Ollama models via JSON config
- **Automatic Text Processing** — Cleans and chunks documents with configurable split parameters
- **File Type Detection** — Routes files to appropriate ingestion pipelines based on MIME type
- **Persistent Vector Storage** — ChromaDB-backed storage with similarity search
- **Registry Pattern** — Centralized model management with lazy loading

## Quick Start

### Installation

```bash
git clone https://github.com/CoffeeCat1920/ragchain.git
cd LangChain
python -m venv .venv
source .venv/bin/activate
pip install langchain-core langchain-chroma langchain-huggingface langchain-ollama langchain-text-splitters
```

### Configuration

Edit `default_config/embedding_model_config.json` to select your embedding model:

```json
{
  "embedding_models_list": {
    "text_embedding_models_list": {
      "huggingface_embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
      "ollama_embedding_model": "locusai/all-minilm-l6-v2"
    }
  },
  "current_text_embedding_model": "OLLAMA_EMBEDDING_MODEL"
}
```

### Usage

```python
from ragchain.vector_store.vector_store import VectorStore

# Initialize with a persistence path
store = VectorStore("chroma_db")

# Ingest a document
store.injust("path/to/document.txt")

# Query for relevant chunks
results = store.retrieve("What is X?", k=3)
for doc in results:
    print(doc.page_content)
```

### CLI

```bash
python -m ragchain
```

## Tech Stack
- **LangChain** — Core framework
- **ChromaDB** — Vector storage
- **HuggingFace / Ollama** — Embedding models
- **Python 3.10+**
