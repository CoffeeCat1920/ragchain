from . import embedding_model_base
from langchain_huggingface import HuggingFaceEmbeddings

class HFTextEMBase(embedding_model_base.EMBase):
    def __init__(self, modelname : str):
        super().__init__()
        self.embedding_model = HuggingFaceEmbeddings(
                model_name=modelname)

    def PrintModelName(self):
        print(self.embedding_model.model_name)

    def GetEmbeddingModel(self):
        return self.embedding_model 
