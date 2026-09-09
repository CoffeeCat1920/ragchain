from dataclasses import dataclass
import json

@dataclass 
class TextEmbeddingModelsList:
    huggingface_embedding_model: str
    ollama_embedding_model: str

@dataclass
class EmbeddingModelsConfig:
    text_embedding_models_list: TextEmbeddingModelsList
    current_text_embedding_model: str

def LoadEmbeddingModelsConfigFromPath(path : str):
    with open(path) as f:
       data = json.load(f)
       text_embedding_models_list = TextEmbeddingModelsList(**data["embedding_models_list"]["text_embedding_models_list"]) 
       current_text_embedding_mode = data["current_text_embedding_model"]
       embedding_models_list = EmbeddingModelsConfig(text_embedding_models_list=text_embedding_models_list, 
                                                   current_text_embedding_model=current_text_embedding_mode)
    return embedding_models_list

def LoadEmbeddingModelConfig():
    return LoadEmbeddingModelsConfigFromPath("./default_config/embedding_model_config.json") 
