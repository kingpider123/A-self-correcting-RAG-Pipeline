# A-self-correcting-RAG-Pipeline
A fault-tolerant, multi-agent retrieval pipeline built with LangGraph to detect and autonomously correct LLM hallucinations prior to user delivery.

## The Problem
Standard Retrieval-Augmented Generation (RAG) pipelines suffer from a critical flaw: they blindly trust the retrieval step. If a vector database returns irrelevant context, or if the LLM suffers from "attention drift," the system will confidently hallucinate an answer. In production environments—especially when querying technical documentation, diagnosing network telemetry, or troubleshooting smart hardware—hallucinating an invalid command or policy is unacceptable.

## The Solution
This project implements an Agentic RAG State Machine that refuses to guess. Instead of a linear script, the pipeline operates as a cyclical graph. It utilizes JSON-constrained LLMs as deterministic "evaluator nodes" to grade relevance and factual consistency. If a hallucination is detected, the system blocks the output, injects targeted feedback into the prompt, and forces the generator to rewrite the answer until it is 100% grounded in the source text.

## Architecture & Data Flow
The pipeline is orchestrated using LangGraph, treating agents as nodes and routing logic as conditional edges:

Retrieval Node: Embeds the user query and fetches semantic matches from a local ChromaDB vector store.

Guardrail Agent (Filter): A strict JSON-output agent that evaluates each retrieved document. It discards irrelevant chunks before they can pollute the generation context.

Generator Agent: Drafts an initial answer using strictly the filtered context.

Evaluator Agent (Hallucination Checker): Performs Natural Language Inference (NLI). It grades the drafted answer against the source documents.

If True (Factual) ➡️ Delivers the answer to the user.

If False (Hallucinated) ➡️ Routes back to the Generator with a feedback warning to try again.

## Tech Stack
Orchestration: LangGraph (State Graphs, Conditional Edges)

LLM: Google Gemini 2.5 Flash (Optimized for low-latency JSON structured output)

Vector Database: ChromaDB (Local SQLite-backed vector store)

Embeddings: HuggingFace sentence-transformers (all-MiniLM-L6-v2)

Language: Python 3.9+