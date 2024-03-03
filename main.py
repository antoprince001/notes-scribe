from typing import Union
from fastapi import FastAPI
from src.notes_scribe.llama_index_query import chat_with_knowledge_base, chat_with_llm, setup_index

app = FastAPI()
query_engine = setup_index(index_dir='src/notes_scribe/indices')


@app.get("/")
def read_root():
    return {"app_name": "Notes-Scribe"}


@app.get("/chat_with_llm")
def read_chat_with_llm(prompt: str = None):
    response = chat_with_llm(prompt)
    return {"response": response}


@app.get("/chat_with_knowledge_base")
def read_chat_with_knowledge_base(prompt: str = None):
    response = chat_with_knowledge_base(prompt, query_engine)
    return {"response": response}