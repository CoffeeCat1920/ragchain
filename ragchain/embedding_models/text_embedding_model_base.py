from . import embedding_model_base
from langchain_core.embeddings import Embeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaEmbeddings

class HFTextEMBase(embedding_model_base.EMBase):
    def __init__(self, model_name : str):
        super().__init__()
        self.embedding_model = HuggingFaceEmbeddings(
                model_name=model_name)

    def print_model_name(self):
        print(self.embedding_model.model_name)

    def get_embedding_model(self) -> Embeddings:
        return self.embedding_model 

class OLTextEMBase(embedding_model_base.EMBase):
    def __init__(self, model_name : str):
        super().__init__()
        self.embedding_model = OllamaEmbeddings(model=model_name) 

    def print_model_name(self):
        print(self.embedding_model.model)

    def get_embedding_model(self) -> Embeddings:
        return self.embedding_model 
