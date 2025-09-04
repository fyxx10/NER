from typing import Tuple

class InputValidator:
    @staticmethod
    def validate_text(text: str) -> Tuple[bool, str]:
        """
        Validate input text.
        
        Args:
            text (str): Text to validate
            
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        if not text:
            return False, "Please enter some text to analyze."
        
        if len(text.strip()) < 3:
            return False, "Text must be at least 3 characters long."
            
        if len(text) > 10000:
            return False, "Text exceeds maximum length of 10,000 characters."
            
        return True, ""
    
    @staticmethod
    def validate_model_selection(model: str) -> Tuple[bool, str]:
        """
        Validate model selection.
        
        Args:
            model (str): Model name to validate
            
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        valid_models = ["en_core_web_sm", "en_core_web_md", "en_core_web_lg"]
        
        if model not in valid_models:
            return False, f"Invalid model selection. Please choose from: {', '.join(valid_models)}"
            
        return True, ""