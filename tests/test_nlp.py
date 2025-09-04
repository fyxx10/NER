import pytest
from services.nlp_service import NLPService, NERResult

def test_nlp_service_initialization():
    service = NLPService()
    assert service.nlp is not None

def test_process_text():
    service = NLPService()
    text = "John works at Microsoft in Seattle."
    result = service.process_text(text)
    
    assert isinstance(result, NERResult)
    assert result.text == text
    assert len(result.entities) > 0
    
    # Check if common entities are detected
    entity_texts = [e["text"] for e in result.entities]
    assert "John" in entity_texts
    assert "Microsoft" in entity_texts
    assert "Seattle" in entity_texts

def test_empty_text():
    service = NLPService()
    result = service.process_text("")
    
    assert isinstance(result, NERResult)
    assert result.text == ""
    assert len(result.entities) == 0