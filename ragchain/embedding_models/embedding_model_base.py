from langchain_core.embeddings import Embeddings

from ragchain.config import embedding_models_config
from abc import ABC, abstractmethod 

class EMBase(ABC):
    def __init__(self):
        self.config = embedding_models_config.LoadEmbeddingModelConfig()

    @abstractmethod
    def print_model_name(self) -> None:
        pass
    
    @abstractmethod
    def get_embedding_model(self) -> Embeddings:
        pass
