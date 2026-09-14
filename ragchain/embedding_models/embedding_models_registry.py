from typing import Dict
from langchain_core.embeddings import Embeddings
from ragchain.config.embedding_models_config import (
    LoadEmbeddingModelConfig,
    TextEMOption,
)
from ragchain.embedding_models.embedding_model_base import EMBase

from .text_embedding_model_base import (
    HFTextEMBase,
    OLTextEMBase,
)

_MODEL_TYPES = {
    TextEMOption.HUGGINGFACE_EMBEDDING_MODEL: HFTextEMBase,
    TextEMOption.OLLAMA_EMBEDDING_MODEL: OLTextEMBase,
}

class EmbeddingRegistry:
    def __init__(self) -> None:
        self.config = LoadEmbeddingModelConfig()
        self.text_models : dict[TextEMOption, EMBase] = {}

        self._load_text_models()

    def _load_text_models(self) -> None:
        for option in TextEMOption:
            model_class = _MODEL_TYPES.get(option)

            if model_class is not None:
                self.text_models[option] = model_class(
                    model_name=self.config.text_embedding_models_list.get(option)
                )

    def _get_text_model(self, option: TextEMOption) -> Embeddings | None:
        emb_model = self.text_models.get(option)
        if emb_model == None:
            return None 
        return emb_model.get_embedding_model()

    def get_current_text_model(self) -> Embeddings | None:
        return self._get_text_model(self.config.current_text_embedding_model)
    
    def print_current_text_model(self) -> None:
        self.get_current_text_model().print_model_name() #type: ignore 
