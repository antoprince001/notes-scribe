# Notes-Scribe

This FastAPI web application leverages Open source LLMs (Large Language Model) using Ollama and LlamaIndex to build a RAG (Retrieval-Augmented Generation) knowledge base on top of notes taken. It provides endpoints for interacting with the knowledge base to get responses to user queries.

## Tech Stack

- **FastAPI**

- **Ollama**

- **LlamaIndex**

## Features

- **Chat with LLM Endpoint**: Use this endpoint to interact with Ollama LLM by providing prompts and receiving responses.
  - Endpoint: `http://localhost:8000/chat_with_llm?prompt=your_prompt_here`
- **Chat with Knowledge Base Endpoint**: Use this endpoint to query the knowledge base built using LlamaIndex and retrieve relevant information.
  - Endpoint: `http://localhost:8000/chat_with_knowledge_base?prompt=your_prompt_here`

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_project.git
    cd your_project
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Add your notes file to the 'data/Courses' directory

4. Run test suite:

    ```bash
    pytest
    ```

5. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

6. Open your web browser and navigate to the provided endpoints to interact with the REST API.
