from . import embedding_model_base
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaEmbeddings

class HFTextEMBase(embedding_model_base.EMBase):
    def __init__(self, model_name : str):
        super().__init__()
        self.embedding_model = HuggingFaceEmbeddings(
                model_name=model_name)

    def PrintModelName(self):
        print(self.embedding_model.model_name)

    def GetEmbeddingModel(self):
        return self.embedding_model 

class OLTextEMBase(embedding_model_base.EMBase):
    def __init__(self, model_name : str):
        super().__init__()
        self.embedding_model = OllamaEmbeddings(model=model_name) 

    def PrintModelName(self):
        print(self.embedding_model.model)

    def GetEmbeddingModel(self):
        return self.embedding_model 
