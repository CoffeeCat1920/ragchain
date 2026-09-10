from dataclasses import dataclass, field 
from enum import Enum
import json

class TextEmbeddingModelOption(Enum):
    HUGGINGFACE_EMBEDDING_MODEL = "huggingface_embedding_model" 
    OLLAMA_EMBEDDING_MODEL = "ollama_embedding_model"

@dataclass 
class TextEmbeddingModelsList:
    text_embedding_models_list: dict = field(default_factory=dict)
    def get(self, text_embedding_model : TextEmbeddingModelOption):
        return self.text_embedding_models_list[text_embedding_model.value] 

@dataclass
class EmbeddingModelsConfig:
    text_embedding_models_list: TextEmbeddingModelsList
    current_text_embedding_model: TextEmbeddingModelOption 

def LoadEmbeddingModelsConfigFromPath(path : str):
    with open(path) as f:
       data = json.load(f)
       text_embedding_models_list = TextEmbeddingModelsList(**data["embedding_models_list"]) 
       current_text_embedding_mode = TextEmbeddingModelOption[ data["current_text_embedding_model"] ]
       embedding_models_list = EmbeddingModelsConfig(text_embedding_models_list=text_embedding_models_list, 
                                                   current_text_embedding_model=current_text_embedding_mode)
    return embedding_models_list

def LoadEmbeddingModelConfig():
    return LoadEmbeddingModelsConfigFromPath("./default_config/embedding_model_config.json") 
