from enum import Enum 
from pydantic import BaseModel

class TextLLMOption(str, Enum):
    HUGGINGFACE="HUGGINGFACE"
    OLLAMA="OLLAMA"

class TextLLMConfig(BaseModel):
    text_llm_list: dict[TextLLMOption, str] 

class LLMConfig(BaseModel):
    text_llm_config : TextLLMConfig 
    current_text_llm: TextLLMOption


def LoadLLMConfig(path : str) -> LLMConfig:
    with open(path) as f:
        config_text = f.read()
        llm_config = LLMConfig.model_validate_json(config_text)
    return llm_config


def LoadDefaultLLMConfig() -> LLMConfig:
    return LoadLLMConfig("./default_config/llm_config.json")
