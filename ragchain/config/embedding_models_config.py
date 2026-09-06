from dataclasses import dataclass
import json

@dataclass 
class TextEmbeddingModelsList:
    huggingface_embedding_model: str
    ollama_embedding_model: str

@dataclass
class EmbeddingModelsList:
    text_embedding_models: TextEmbeddingModelsList

def LoadEmbeddingModelsList(path : str):
    with open(path) as f:
       data = json.load(f)
       text_embedding_models_list = TextEmbeddingModelsList(**data["text_embedding_models"]) 
       embedding_models_list = EmbeddingModelsList(text_embedding_models=text_embedding_models_list)
    return embedding_models_list
