from dataclasses import dataclass
from typing import List, Dict, Any
import spacy
from utils.constants import DEFAULT_MODEL

@dataclass
class NERResult:
    text: str
    entities: List[Dict[str, Any]]

class NLPService:
    def __init__(self, model_name: str = DEFAULT_MODEL):
        try:
            self.nlp = spacy.load(model_name)
        except OSError:
            raise RuntimeError(f"Failed to load model '{model_name}'. Please ensure it's installed.")
    
    def process_text(self, text: str) -> NERResult:
        """
        Process input text and extract named entities.
        
        Args:
            text (str): Input text to process
            
        Returns:
            NERResult: Processed text and extracted entities
        """
        doc = self.nlp(text)
        entities = self.get_entities(doc)
        return NERResult(text=text, entities=entities)
    
    def get_entities(self, doc) -> List[Dict[str, Any]]:
        """
        Extract entities from processed document.
        
        Args:
            doc: spaCy document object
            
        Returns:
            List[Dict]: List of extracted entities with their details
        """
        return [
            {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char
            }
            for ent in doc.ents
        ]