import pytest
from unittest.mock import MagicMock, patch
from src.notes_scribe.llama_index_query import setup_index, chat_with_knowledge_base, chat_with_llm

@pytest.fixture
def mock_query_engine():
    query_engine = MagicMock()
    query_engine.query.return_value = "Mocked result"
    return query_engine

def test_chat_with_knowledge_base(mock_query_engine):
    # Mock the query engine
    query_engine = mock_query_engine
    
    # Call the function under test
    result = chat_with_knowledge_base("what is unit test", query_engine)
    
    # Assert the result
    assert result == "Mocked result"

@patch('src.notes_scribe.llama_index_query.llm')
def test_chat_with_llm(mock_llm):
    # Mock the llm object
    mock_llm.complete.return_value = "Mocked response"
    
    # Call the function under test
    result = chat_with_llm("What is unit test")
    
    # Assert the result
    assert result == "Mocked response"