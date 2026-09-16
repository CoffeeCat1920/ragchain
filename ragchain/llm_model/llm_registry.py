from ragchain.config.text_llm_config import LLMConfig, LoadDefaultLLMConfig, TextLLMOption 
from .llm_base import LLMBase
from .llm_ollama import LLMBaseOllama

_MODEL_LIST = {
        TextLLMOption.OLLAMA: LLMBaseOllama
}

class LLMModelRegistry():
    def __init__(self):
        self.config : LLMConfig = LoadDefaultLLMConfig()
        self.text_models : dict[TextLLMOption, LLMBase] = {}
        self._load_text_models()
    
    def _load_text_models(self) -> None:
        for option in TextLLMOption:
            model_class = _MODEL_LIST.get(option)
            if model_class != None:
                self.text_models[option] = model_class(
                        model_name=self.config.get(option)
                        )

    def current_text_model(self) -> LLMBase:
        return self.text_models[self.config.current_text_llm]
