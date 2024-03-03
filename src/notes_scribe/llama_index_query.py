from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from transformers import AutoTokenizer
from llama_index.core import set_global_tokenizer
from llama_index.core import ServiceContext
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from pathlib import Path

llm = Ollama(model="openhermes", request_timeout=30.0)

embedding_model = HuggingFaceEmbedding(model_name="WhereIsAI/UAE-Large-V1")  # https://huggingface.co/WhereIsAI/UAE-Large-V1

set_global_tokenizer(
    AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1").encode  # pass in the HuggingFace model org + repo
)

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embedding_model,
    system_prompt='You are a bot that answers questions about notes taken by a data engineering consultant'
)


def setup_index(index_dir):
    index_exists = any(item for item in Path(index_dir).iterdir() if item.name != '.gitkeep')  # Checks if the directory is not empty
    if index_exists:
        storage_context = StorageContext.from_defaults(persist_dir=index_dir)
        index = load_index_from_storage(storage_context, service_context=service_context)
    else:
        documents = SimpleDirectoryReader("src/notes_scribe/data/notes").load_data()
        index = VectorStoreIndex.from_documents(documents, service_context=service_context, show_progress=True)
        index.storage_context.persist(persist_dir=index_dir)
    query_engine = index.as_query_engine()
    return query_engine


def chat_with_knowledge_base(query, query_engine):
    result = query_engine.query(query)
    return result


def chat_with_llm(prompt):
    try:
        if prompt is None or len(prompt) < 1:
            return "Input missing for LLM"
        resp = llm.complete(prompt)
        return resp
    except Exception as e:
        print(e)
        return "Error generating response !"
