# Gen AI Learning Project

This repository is a hands-on learning journey for building Generative AI applications.

## Learning Roadmap

### 1. Tokenization with Tiktoken

[Tiktoken](https://github.com/openai/tiktoken) is a fast library for converting text into tokens. Understanding tokenization is important because language models process token IDs rather than raw text.

Topics to explore:
- Text encoding and decoding
- Model-specific encodings
- Token counts and context-window limits
- Comparing tokenization across words, code, and other languages

### 2. Text Embeddings with Sentence Transformers

[Sentence Transformers](https://www.sbert.net/) is used to convert sentences and documents into dense vector embeddings. These vectors capture semantic meaning and allow machines to compare text based on meaning rather than exact words.

Topics to explore:
- Generating embeddings
- Measuring similarity with cosine similarity
- Semantic search
- Clustering and recommendation systems
- Building a small vector-search prototype

### 3. Working with Large Language Models

After understanding tokens and embeddings, the project will progress to accessing and building applications with Large Language Models (LLMs).

Planned topics:
- Calling hosted and local LLM APIs
- Prompt engineering
- Chat and completion patterns
- Retrieval-Augmented Generation (RAG)
- Conversation memory
- Tools and agent workflows
- Evaluation, safety, and responsible AI

## Getting Started

Install the initial dependencies:

```bash
pip install tiktoken sentence-transformers openai
```

## Current Example

`ai.py` demonstrates basic text encoding with Tiktoken:

- Loads the `o200k_base` encoding
- Encodes the text `I love AI`
- Prints its token IDs

Run it with:

```bash
python ai.py
```

## Project Goals

1. Learn how text is prepared for language models.
2. Understand embeddings and semantic similarity.
3. Build increasingly practical LLM applications.
4. Experiment with RAG, agents, evaluation, and real-world use cases.
