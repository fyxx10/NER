import streamlit as st
from services.nlp_service import NERResult
from typing import Optional

class TextInputComponent:
    def render(self) -> Optional[str]:
        """
        Render text input area.
        
        Returns:
            Optional[str]: Input text if provided, None otherwise
        """
        return st.text_area(
            "Enter text for NER analysis",
            height=150,
            help="Enter the text you want to analyze for named entities."
        )

class ResultsDisplayComponent:
    def render(self, ner_result: NERResult) -> None:
        """
        Display NER results.
        
        Args:
            ner_result (NERResult): Results to display
        """
        if not ner_result.entities:
            st.info("No entities found in the text.")
            return
            
        st.subheader("Found Entities:")
        
        # Create a color map for entity types
        entity_colors = {}
        
        for entity in ner_result.entities:
            if entity["label"] not in entity_colors:
                entity_colors[entity["label"]] = len(entity_colors)
            
            st.markdown(
                f'<span style="background-color: hsl({entity_colors[entity["label"]] * 50}, 70%, 80%)">'
                f'{entity["text"]}</span> - {entity["label"]}',
                unsafe_allow_html=True
            )