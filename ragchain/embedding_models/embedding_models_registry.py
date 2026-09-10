from ragchain.config.embedding_models_config import (
    LoadEmbeddingModelConfig,
    TextEMOption,
    TextEmbeddingModelsList,
)

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
        self.text_models = {}

        self._load_text_models()

    def _load_text_models(self) -> None:
        for option, model_name in TextEmbeddingModelsList.text_embedding_models_list:
            model_class = _MODEL_TYPES.get(option)

            if model_class is not None:
                self.text_models[option] = model_class(
                    model_name=model_name
                )

    def get_text_model(self, option: TextEMOption):
        return self.text_models.get(option)
