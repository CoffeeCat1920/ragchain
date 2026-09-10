from langchain_core.embeddings import Embeddings
from ragchain.config import embedding_models_config
from . import embedding_model_base, text_embedding_model_base
from dataclasses import field 

class EMDirectory():
    def __load_text_models__(self):
        for model_option, model_name in embedding_models_config.TextEmbeddingModelsList.text_embedding_models_list:
            if model_option == embedding_models_config.TextEMOption.HUGGINGFACE_EMBEDDING_MODEL:
                self.text_models[model_option] = text_embedding_model_base.HFTextEMBase(modelname=model_name)
            

    def __init__(self) -> None:
        self.config = embedding_models_config.LoadEmbeddingModelConfig()
        self.text_models: dict = field(default_factory=dict)
        self.__load_text_models__()
    
    # def GetCurrentEmbeddingModel() -> Embeddings:
    #     pass
