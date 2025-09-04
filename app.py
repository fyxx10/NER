import streamlit as st
from services.nlp_service import NLPService
from ui.components import TextInputComponent, ResultsDisplayComponent
from utils.validators import InputValidator

def main():
    st.title("Named Entity Recognition System")
    
    # Initialize services
    nlp_service = NLPService()
    text_input = TextInputComponent()
    results_display = ResultsDisplayComponent()
    
    # Get user input
    input_text = text_input.render()
    
    if input_text:
        # Validate input
        is_valid, error_msg = InputValidator.validate_text(input_text)
        
        if not is_valid:
            st.error(error_msg)
            return
            
        try:
            # Process text
            ner_result = nlp_service.process_text(input_text)
            
            # Display results
            results_display.render(ner_result)
            
        except Exception as e:
            st.error(f"An error occurred during processing: {str(e)}")

if __name__ == "__main__":
    main()