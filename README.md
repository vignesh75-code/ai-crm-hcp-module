# AI CRM HCP Interaction Module

## Overview
AI-powered CRM assistant designed to help pharmaceutical representatives interact with Healthcare Professionals (HCPs).

The system uses an AI agent built with LangGraph to process queries and generate intelligent responses.
## System Architecture

User (Browser)
        │
        ▼
Frontend (HTML + JavaScript)
        │
        ▼
FastAPI Backend (Python)
        │
        ▼
LangGraph Agent
        │
        ▼
Tools Layer
        │
        ▼
Groq LLM API

## Tech Stack
Backend:
- Python
- FastAPI
- LangGraph
- Groq API

Frontend:
- HTML
- JavaScript

## Project Structure

backend/
  main.py
  requirements.txt
  langgraph_agent/
    agent.py
    tools.py

frontend/
  index.html

## How to Run

Install dependencies:

pip install -r backend/requirements.txt

Run backend:

python backend/main.py

Open frontend:

Open frontend/index.html in browser

## API Endpoints

### POST /chat
Sends a user message to the AI agent and returns a response.

Request Example:
{
  "message": "Tell me about Product X"
}

Response Example:
{
  "response": "Product X is used for..."
}

### GET /interactions
Returns past interaction history.

Response Example:
[
  {
    "user": "What is Drug A?",
    "ai": "Drug A is used for..."
  }
]

## AI Agent Workflow

1. User sends a query through the frontend.
2. FastAPI backend receives the request.
3. The LangGraph agent processes the query.
4. The agent selects appropriate tools.
5. Tools fetch or generate information.
6. Response is returned to the frontend.