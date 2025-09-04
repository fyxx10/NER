import pytest
from utils.validators import InputValidator

def test_text_validation():
    # Test empty text
    is_valid, msg = InputValidator.validate_text("")
    assert not is_valid
    assert "enter some text" in msg.lower()
    
    # Test short text
    is_valid, msg = InputValidator.validate_text("ab")
    assert not is_valid
    assert "3 characters" in msg.lower()
    
    # Test valid text
    is_valid, msg = InputValidator.validate_text("This is a valid text.")
    assert is_valid
    assert msg == ""
    
    # Test too long text
    long_text = "a" * 10001
    is_valid, msg = InputValidator.validate_text(long_text)
    assert not is_valid
    assert "maximum length" in msg.lower()

def test_model_validation():
    # Test valid model
    is_valid, msg = InputValidator.validate_model_selection("en_core_web_sm")
    assert is_valid
    assert msg == ""
    
    # Test invalid model
    is_valid, msg = InputValidator.validate_model_selection("invalid_model")
    assert not is_valid
    assert "Invalid model selection" in msg