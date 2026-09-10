from langchain_core.embeddings import Embeddings

from ragchain.config import embedding_models_config
from abc import ABC, abstractmethod 

class EMBase(ABC):
    def __init__(self):
        self.config = embedding_models_config.LoadEmbeddingModelConfig()

    @abstractmethod
    def PrintModelName(self):
        pass
    
    @abstractmethod
    def GetEmbeddingModel(self) -> Embeddings:
        pass
